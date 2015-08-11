from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from django.core.serializers import get_serializer
from .models import Client, Company
from est_quote.forms import QuoteCreateForm

@login_required
def client_view(request):
    if request.method == 'POST':
        if 'client' in request.POST:
            client = Client.objects.get(id=request.POST['client'])
        else:
            client = Client()

        client.company = Company.objects.get(id=int(request.POST['company']))
        client.first_name = request.POST['first_name']
        client.last_name = request.POST['last_name']
        client.title = request.POST['title']
        client.cell = request.POST['cell']
        client.desk = request.POST['desk']
        client.email = request.POST['email']

        client.save()

        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])
