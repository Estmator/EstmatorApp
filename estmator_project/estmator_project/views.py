from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic import TemplateView

from est_client.forms import ClientCreateForm
from est_quote.forms import QuoteCreateForm, ClientListForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context


@login_required
def menu_view(request):
    if request.method == 'GET':
        client_form = ClientCreateForm()
        quote_form = QuoteCreateForm()
        client_list_form = ClientListForm()
        context = {
            'client_form': client_form.as_p,
            'quote_form': quote_form.as_p,
            'client_list_form': client_list_form.as_p
        }
        return render(
            request, 'menu.html', context
        )
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def connection_test(request):
    return HttpResponse(status=204)
