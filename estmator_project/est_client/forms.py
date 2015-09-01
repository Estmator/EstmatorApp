from django.forms import ModelForm, Select, TextInput
from .models import Client, Company


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            'company',
            'first_name',
            'last_name',
            'title',
            'cell',
            'desk',
            'email'
        ]
        widgets = {
            'company': Select(attrs={'required': True}),
        }


class CompanyCreateForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'phone',
            'address',
            'address2',
            'city',
            'state',
            'postal',
            'st_rate',
            'ot_rate'
        ]
        widgets = {
            'company_name': TextInput(attrs={'required': True}),
        }


class CompanyListForm(ModelForm):
    class Meta:
        model = Client
        fields = ['company']
