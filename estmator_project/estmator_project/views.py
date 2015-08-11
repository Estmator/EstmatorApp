from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.core.urlresolvers import reverse
from est_quote.models import Quote, Category, Product, ProductInQuote
from est_quote.forms import QuoteCreateForm
from est_client.models import Client, Company
from est_client.forms import ClientCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class QuoteView(TemplateView):
    template_name = 'quote.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.all()
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        context['prods_in_quote'] = ProductInQuote.objects.all()
        return context


@login_required
def menu_view(request):
    if request.method == 'GET':
        client_form = ClientCreateForm()
        quote_form = QuoteCreateForm()
        context = {
            'client_form': client_form.as_p,
            'quote_form': quote_form.as_p
        }
        return render(
            request, 'menu.html', context
        )
    else:
        return HttpResponseNotAllowed(['GET'])
