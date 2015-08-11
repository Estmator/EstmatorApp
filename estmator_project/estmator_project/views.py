from django.views.generic import TemplateView
from est_quote.models import Quote, Category, Product, ProductProperties


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
        context['prods_in_quote'] = ProductProperties.objects.all()
        return context


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        return context
