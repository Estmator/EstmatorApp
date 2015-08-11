from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
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
        print self.request.GET
        try:
            context = super(QuoteView, self).get_context_data(**kwargs)
            context['quotes'] = Quote.objects.all()
            context['categories'] = Category.objects.all()
            context['products'] = Product.objects.all()
            context['prods_in_quote'] = ProductInQuote.objects.all()
            context['quote_client'] = self.request.GET.get('client')
            context['quote_name'] = self.request.GET.get('name')
        except (KeyError, ValueError):
            return redirect('menu')

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
        return HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def quote_form_view(request):
    if request.method == 'GET':
        quote_form = QuoteCreateForm()
        return HttpResponse(quote_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])
