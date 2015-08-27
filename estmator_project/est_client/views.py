from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed

from est_client.models import Client, Company
from est_client.forms import (ClientCreateForm, CompanyCreateForm,
                              CompanyListForm)
from est_quote.forms import ClientListForm


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


@login_required
def client_form_view(request):
    if request.method == 'GET':
        client_form = ClientCreateForm()
        return HttpResponse(client_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def client_edit_form_view(request):
    if request.method == 'GET':
        client = Client.objects.get(id=request.GET['pk'])
        client_form = ClientCreateForm(instance=client)
        return HttpResponse(client_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def client_list_form_view(request):
    if request.method == 'GET':
        client_list_form = ClientListForm()
        return HttpResponse(client_list_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def company_view(request):
    if request.method == 'POST':
        if 'company' in request.POST:
            company = Company.objects.get(id=request.POST['company'])
        else:
            company = Company()

        company.company_name = request.POST['company_name']
        company.phone = request.POST['phone']
        company.address = request.POST['address']
        company.address2 = request.POST['address2']
        company.city = request.POST['city']
        company.postal = request.POST['postal']
        company.st_rate = request.POST['st_rate']
        company.ot_rate = request.POST['ot_rate']

        company.save()

        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def company_form_view(request):
    if request.method == 'GET':
        company_form = CompanyCreateForm()
        return HttpResponse(company_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def company_edit_form_view(request):
    if request.method == 'GET':
        company = Company.objects.get(id=request.GET['pk'])
        company_form = CompanyCreateForm(instance=company)
        return HttpResponse(company_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])


@login_required
def company_list_form_view(request):
    if request.method == 'GET':
        company_list_form = CompanyListForm()
        return HttpResponse(company_list_form.as_p())
    else:
        return HttpResponseNotAllowed(['GET'])
