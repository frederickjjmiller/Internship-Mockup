from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, render
from django.core.exceptions import ObjectDoesNotExist

from .forms import SearchSelection

from .models import NetDevice


def get_device(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        search_select = SearchSelection(request.POST)
        # check whether it's valid:
        if search_select.is_valid():
            search_param = search_select.cleaned_data['search_param']
            search_term = search_select.cleaned_data['search_term']
            if search_param == "AT":
                # Check if device is in database, if does not exist, check SN, ND, & Airwave
                # redirect to a new URL:
                url = "/report/device/" + search_term
                return HttpResponseRedirect(url)
            elif search_param == "IP":
                # Check if device is in database, if does not exist, check SN, ND, & Airwave
                # redirect to a new URL:
                url = "/report/address/" + search_term
                return HttpResponseRedirect(url)
            elif search_param == "SN":
                # Check if device is in database, if does not exist, check SN, ND, & Airwave
                # redirect to a new URL:
                url = "/report/serial/" + search_term
                return HttpResponseRedirect(url)

    # if a GET (or any other method) we'll create a blank form
    else:
        search_select = SearchSelection(request.POST)

    return render(request, 'report/device.html', {'search_select': search_select})


def device_report(request, device):
    # request the device from the database
    try:
        requested_device = NetDevice.objects.get(asset_tag=device)
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
        requested_device = NetDevice.objects.get(ip_address=address)
        if requested_device.is_wireless:
            template = loader.get_template('report/wireless_report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('report/wired-report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        message = address + " DOESNT EXIST"
        return HttpResponse(message)


def serial_report(request, serial):
    # request the device from the database
    try:
        requested_device = NetDevice.objects.get(serial_number=serial)
        if requested_device.is_wireless:
            template = loader.get_template('report/wireless_report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('report/wired-report.html')
            context = {'device': requested_device}
            return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        message = serial + " DOESNT EXIST"
        return HttpResponse(message)




