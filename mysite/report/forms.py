# Built Following the tutorial at https://docs.djangoproject.com/en/2.0/topics/forms/

from django import forms


class DeviceForm(forms.Form):
    asset_tag = forms.CharField(label='Device Asset Tag', max_length=100)


class IPForm(forms.Form):
    ip_address = forms.CharField(label='Device IP Address', max_length=100)


class SearchSelection(forms.Form):
    search_param = forms.ChoiceField(label="Search by:   ", required=False, choices=(
    ('AT', 'Asset Tag'),
    ('IP', 'IP Address'),
    ('SN', 'Serial Number'),
))
    search_term = forms.CharField(max_length=100, required=False, label="Search for:   ")

    class Meta:
        fields = ('search_param', 'search_term')