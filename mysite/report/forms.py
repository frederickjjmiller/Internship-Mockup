# Built Following the tutorial at https://docs.djangoproject.com/en/2.0/topics/forms/

from django import forms


class DeviceForm(forms.Form):
    asset_tag = forms.CharField(label='Device Asset Tag', max_length=100)

