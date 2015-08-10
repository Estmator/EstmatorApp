from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    # user = forms.CharField(max_length=256)
    # category = forms.CharField(max_length=256)
    # products = forms.CharField(max_length=256)

    class Meta:
        model = Quote
        fields = ['name', 'category', 'products']

    def save(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.instance.user.save()
        return super(QuoteForm, self).save(*args, **kwargs)
