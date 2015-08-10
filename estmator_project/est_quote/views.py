from django.forms.formsets import formset_factory
from django.views.generic.edit import FormView
from .forms import QuoteForm


class QuoteCreateView(FormView):
    template_name = 'quote.html'
    form_class = QuoteForm
    success_url = '/'
    QuoteFormSet = formset_factory(QuoteForm)
    formset = QuoteFormSet()

    # def get_form(self, form_class=QuoteForm):
    #     # quote = Quote.objects.get(user=self.request.user)
    #     return QuoteForm(instance=quote, **self.get_form_kwargs())

    # def get_form_kwargs(self):
    #     kwargs = super(QuoteCreateView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    # def form_valid(self, form):
    #     quote = form.save(commit=False, request=self.request)
    #     quote.user = self.request.user
    #     quote.save()
    #     return super(QuoteCreateView, self).form_valid(quote)
