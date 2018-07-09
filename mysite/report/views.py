from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, render
from django.core.exceptions import ObjectDoesNotExist

from .forms import DeviceForm, IPForm

from .models import Device


def get_device(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        device_form = DeviceForm(request.POST)
        ip_form = IPForm(request.POST)
        # check whether it's valid:
        if device_form.is_valid():
            # process the data in form.cleaned_data as required
            query = device_form.cleaned_data['asset_tag']
            # this is where we check the database for the device
            # then check how recent the data is
            # redirect to a new URL:
            url = "/report/device/" + query
            return HttpResponseRedirect(url)
        elif ip_form.is_valid():
            # process the data in form.cleaned_data as required
            query = ip_form.cleaned_data['ip_address']
            # this is where we check the database for the device
            # then check how recent the data is
            # redirect to a new URL:
            url = "/report/address/" + query
            return HttpResponseRedirect(url)

    # if a GET (or any other method) we'll create a blank form
    else:
        device_form = DeviceForm(request.GET)
        ip_form = IPForm(request.GET)

    return render(request, 'report/device.html', {'device_form': device_form, 'ip_form': ip_form})


def device_report(request, device):
    # request the device from the database
    try:
        requested_device = Device.objects.get(asset_tag=device)
        if requested_device.is_wireless:
            template = loader.get_template('report/wireless_report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('report/wired-report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        message = device + " DOESNT EXIST"
        return HttpResponse(message)


def ip_report(request, address):
    # request the device from the database
    try:
        requested_device = Device.objects.get(ip_address=address)
        template = loader.get_template('report/wireless_report.html')
        context = {'device': requested_device}
        return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        message = address + " DOESNT EXIST"
        return HttpResponse(message)




