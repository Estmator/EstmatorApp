from django.forms.formsets import BaseFormSet
from django import forms
from .models import Quote, Product, Category


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'category', 'products']


class QuoteFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(QuoteFormSet, self).add_fields(form, index)
        form.fields['name'] = forms.CharField(max_length=128)
        form.fields['category'].queryset = Category.objects.all()
        form.fields['products'].queryset = Product.objects.all()
