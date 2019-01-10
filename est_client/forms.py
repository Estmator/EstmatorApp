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
            'first_name': TextInput(attrs={'required': True}),
            'last_name': TextInput(attrs={'required': True}),
            'title': TextInput(attrs={'required': True}),
            'cell': TextInput(attrs={'required': True}),
            'email': TextInput(attrs={'required': True}),
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
            'phone': TextInput(attrs={'required': True}),
            'address': TextInput(attrs={'required': True}),
            'city': TextInput(attrs={'required': True}),
            'postal': TextInput(attrs={'required': True}),
        }


class CompanyListForm(ModelForm):
    class Meta:
        model = Client
        fields = ['company']
