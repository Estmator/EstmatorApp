# from django import forms
# from .models import Quote, Product, Category


# class QuoteForm(forms.ModelForm):
#     class Meta:
#         model = Quote
#         fields = ['name', 'date', 'category', 'products']



# class ProfileSettingsForm(forms.ModelForm):
#     first_name = forms.CharField(label='First Name', max_length=36)
#     last_name = forms.CharField(label='Last Name', max_length=36)
#     email = forms.EmailField(label='Email')

#     class Meta:
#         model = ImagerProfile
#         fields = ['address', 'fav_camera', 'photo_type', 'url']

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop("request")
#         super(ProfileSettingsForm, self).__init__(*args, **kwargs)
#         try:
#             self.fields['first_name'].initial = self.instance.user.first_name
#             self.fields['last_name'].initial = self.instance.user.last_name
#             self.fields['email'].initial = self.instance.user.email
#         except:
#             pass

#     def save(self, *args, **kwargs):
#         self.request = kwargs.pop("request")
#         self.instance.user.first_name = self.cleaned_data.get('first_name')
#         self.instance.user.last_name = self.cleaned_data.get('last_name')
#         self.instance.user.email = self.cleaned_data.get('email')
#         self.instance.user.save()
#         return super(ProfileSettingsForm, self).save(*args, **kwargs)
