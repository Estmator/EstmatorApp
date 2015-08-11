from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from .models import Client, Company

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
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])
