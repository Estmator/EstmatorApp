from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import render_to_string

from est_client.models import Client
from est_quote.forms import QuoteCreateForm, QuoteOptionsForm
from est_quote.models import Quote, Category, Product, ProductProperties


@login_required
def quote_view(request):
    if request.method == 'POST':
        categories = {c: {p: 0 for p in c.product_set.all()} for c in Category.objects.all()}
        if 'quote' in request.POST:
            quote = Quote.objects.get(id=request.POST['quote'])
            quote_name = quote.name
            for prop in quote.productproperties_set.all():
                categories[prop.product.category][prop.product] = prop.count
        else:
            quote = None
            quote_name = request.POST['name']

        form_html = ''
        options_form = QuoteOptionsForm(instance=quote)

        for fieldname, field in options_form.fields.items():
            form_html += '<li><a>'
            form_html += str(options_form[fieldname]) + ' '
            form_html += options_form[fieldname].label
            form_html += '</a></li>'

        context = {
            'categories': categories,
            'options_form': form_html,
            'client': Client.objects.get(id=request.POST['client']),
            'quote_name': quote_name
        }
        return render(
            request, 'quote.html', context
        )
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def quote_form_view(request):
    if request.method == 'GET':
        quote_form = QuoteCreateForm()
        return HttpResponse(quote_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def quote_edit_form_view(request):
    if request.method == 'GET':
        client = Client.objects.get(id=request.GET['pk'])
        return HttpResponse(client.quotes_select_html())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def review_quote_view(request):
    context = {}
    if request.method == 'POST':
        quote = Quote()

        quote.user = request.user
        quote.client = Client.objects.get(id=request.POST['quote_client'])
        quote.name = request.POST['quote_name']
        quote.sub_total = request.POST['sub_total']
        quote.grand_total = request.POST['grand_total']
        if 'travel_time' in request.POST and request.POST['travel_time'] != '':
            quote.travel_time = request.POST['travel_time']
        else:
            quote.travel_time = 0

        quote.org_street_load = 'org_street_load' in request.POST
        quote.org_midrise_elev_std = 'org_midrise_elev_std' in request.POST
        quote.org_midrise_elv_frt = 'org_midrise_elv_frt' in request.POST
        quote.org_highrise = 'org_highrise' in request.POST
        quote.org_stairs = 'org_stairs' in request.POST
        quote.org_lng_psh = 'org_lng_psh' in request.POST

        quote.dest_street_load = 'dest_street_load' in request.POST
        quote.dest_midrise_elev_std = 'dest_midrise_elev_std' in request.POST
        quote.dest_midrise_elv_frt = 'dest_midrise_elv_frt' in request.POST
        quote.dest_highrise = 'dest_highrise' in request.POST
        quote.dest_stairs = 'dest_stairs' in request.POST
        quote.dest_lng_psh = 'dest_lng_psh' in request.POST

        quote.save()
        products = request.POST.getlist('product')
        counts = [int(x) for x in request.POST.getlist('product_count')]

        context['categories'] = {c: [] for c in Category.objects.all()}
        for i, count in enumerate(counts):
            if count > 0:
                prop = ProductProperties()
                prop.quote = quote
                prop.product = Product.objects.get(id=int(products[i]))
                prop.count = count
                prop.save()

                quote.productproperties_set.add(prop)
                context['categories'][prop.product.category].append((prop.product, count))

        quote.save()
        context['quote'] = quote
        context['straight_time_cost'] = request.POST['straight_time_cost']
        context['over_time_cost'] = request.POST['over_time_cost']

        """
        Duplicating getting the categories/products/counts for the
        context because I can't figure out what the above is doing?

        Will try again when I get some sleep.
        """
        context['categories'] = None
        quote_products = ProductProperties.objects.filter(quote=quote)
        categories = {}

        for c in Category.objects.all():
            categories[c.name] = []
            for qp in quote_products:
                if qp.product.category == c:
                    categories[c.name].append({
                        'name': qp.product.name,
                        'count': qp.count
                    })
        """
        figure out better way to only include the needed categories
        """
        for c in categories.keys():
            if categories[c] == []:
                del categories[c]

        context['categories'] = categories
        context['st'] = float(quote.grand_total) / 60 * float(quote.client.company.st_rate)
        context['ot'] = float(quote.grand_total) / 60 * float(quote.client.company.ot_rate)

    return render(
        request, 'review.html', context
    )


@login_required
def send_quote(request, **kwargs):
    context = {}
    if request is not None:
        context = RequestContext(request, context)

    quote = Quote.objects.get(pk=kwargs.get('pk'))
    client = Client.objects.get(pk=quote.client.pk)

    context['token'] = quote.token
    context['site'] = get_current_site(request)
    context['client'] = client
    context['quote'] = quote
    context['user'] = quote.user

    subject = "Your estmator quote!"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = client.email

    message_txt = render_to_string('email_quote_link.txt', context)

    email_message = EmailMultiAlternatives(
        subject,
        message_txt,
        from_email,
        [to_email]
    )

    if getattr(settings, 'USE_HTML_TEMPLATES', True):
        try:
            message_html = render_to_string('email_quote_link.html', context)
        except TemplateDoesNotExist:
            pass
        else:
            email_message.attach_alternative(message_html, 'text/html')

    email_message.send()

    return redirect(quote_from_token, quote.token)


def quote_from_token(request, **kwargs):
    context = {}

    quote = Quote.objects.get(token=kwargs.get('token'))
    context['quote'] = quote

    quote_products = ProductProperties.objects.filter(quote=quote)
    categories = {}

    for c in Category.objects.all():
        categories[c.name] = []
        for qp in quote_products:
            if qp.product.category == c:
                categories[c.name].append({
                    'name': qp.product.name,
                    'count': qp.count
                })
    """
    figure out better way to only include the needed categories
    """
    for c in categories.keys():
        if categories[c] == []:
            del categories[c]

    context['categories'] = categories
    context['st'] = float(quote.grand_total) / 60 * float(quote.client.company.st_rate)
    context['ot'] = float(quote.grand_total) / 60 * float(quote.client.company.ot_rate)
    return render(
        request, 'review.html', context
    )
