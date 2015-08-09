from .models import Quote, Category, Product
from django.views.generic.edit import CreateView, UpdateView


class QuoteCreateView(CreateView):
    model = Quote
    fields = ['name']
    template_name = 'quote.html'
    success_url = '/'

    def get_form(self, form):
        form = super(QuoteCreateView, self).get_form()
        form.fields['category'].queryset = Category.objects.all()
        form.fields['products'].queryset = Product.objects.all()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuoteCreateView, self).form_valid(form)


class QuoteEditView(UpdateView):
    model = Quote
    fields = ['name']
    template_name = 'quote.html'
    success_url = '/'

    def get_form(self, form):
        form = super(QuoteEditView, self).get_form()
        form.fields['category'].queryset = Category.objects.all()
        form.fields['products'].queryset = Product.objects.all()
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuoteEditView, self).form_valid(form)
