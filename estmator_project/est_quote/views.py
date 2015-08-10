from django.views.generic import TemplateView
from .models import *


class QuoteCreateView(TemplateView):
    template_name = 'quote.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteCreateView, self).get_context_data(**kwargs)
        context['quote'] = Quote.objects.all()
        context['category'] = Category.objects.all()
        context['product'] = Product.objects.all()
        context['prod_in_quote'] = ProductInQuote.objects.all()
        return context
