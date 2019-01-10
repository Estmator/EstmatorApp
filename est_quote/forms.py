from django.forms import ModelForm, Select, TextInput
from .models import Quote


class QuoteCreateForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['client', 'name']
        widgets = {
            'client': Select(attrs={'required': True}),
            'name': TextInput(attrs={'required': True})
        }


class ClientListForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['client']
        widgets = {
            'client': Select(attrs={'required': True}),
        }


class QuoteOptionsForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['travel_time',
                  'org_street_load',
                  'org_midrise_elev_std',
                  'org_midrise_elv_frt',
                  'org_highrise',
                  'org_stairs',
                  'org_lng_psh',
                  'dest_street_load',
                  'dest_midrise_elev_std',
                  'dest_midrise_elv_frt',
                  'dest_highrise',
                  'dest_stairs',
                  'dest_lng_psh'
                  ]
