# Built Following the tutorial at https://docs.djangoproject.com/en/2.0/topics/forms/

from django import forms


class DeviceForm(forms.Form):
    asset_tag = forms.CharField(label='Device Asset Tag', max_length=100)


class IPForm(forms.Form):
    ip_address = forms.CharField(label='Device IP Address', max_length=100)

