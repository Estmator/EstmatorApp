from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class MakeQuoteView(TemplateView):
    template_name = 'quote.html'

    def get_context_data(self, **kwargs):
        context = super(MakeQuoteView, self).get_context_data(**kwargs)
        return context
