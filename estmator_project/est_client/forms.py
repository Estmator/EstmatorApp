from django import forms
from .models import Client, Company


class ClientCreateForm(forms.ModelForm):
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


class CompanyCreateForm(forms.ModelForm):
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


class CompanyListForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company']
