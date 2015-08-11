from django import forms
from .models import Quote


class QuoteCreateForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['client', 'name']
