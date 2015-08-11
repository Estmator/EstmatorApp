from django import forms
from .models import Client


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company',
                  'first_name',
                  'last_name',
                  'title',
                  'cell',
                  'desk',
                  'email']
