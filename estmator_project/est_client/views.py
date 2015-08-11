from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from django.core.serializers import get_serializer
from .models import Client, Company
from est_quote.forms import QuoteCreateForm

@login_required
def client_view(request):
    if request.method == 'POST':
        client = Client(
            company=Company.objects.get(id=int(request.POST['company'])),
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            title=request.POST['title'],
            cell=request.POST['cell'],
            desk=request.POST['desk'],
            email=request.POST['email']
        )
        client.save()

        # JSONSerializer = get_serializer('json')
        # serializer = JSONSerializer()
        #
        # quote_form = QuoteCreateForm()
        # rendered_forms = {
        #     'new_quote': quote_form.as_p()
        # }
        # json_data = serializer.serialize(rendered_forms)
        # return HttpResponse(json_data, content_type='application/json')
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])
