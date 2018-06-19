from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, render
from django.core.exceptions import ObjectDoesNotExist

from .forms import DeviceForm

from .models import Device


def get_device(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeviceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            query = form.cleaned_data['asset_tag']
            # this is where we check the database for the device
            # then check how recent the data is
            # redirect to a new URL:
            url = "/report/device/" + query
            return HttpResponseRedirect(url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeviceForm(request.GET)

    return render(request, 'report/device.html', {'form': form})


def device_report(request, device):
    # request the device from the database
    try:
        requested_device = Device.objects.get(asset_tag=device)
        template = loader.get_template('report/report.html')
        context = {'device': requested_device}
        return HttpResponse(template.render(context, request))
    except ObjectDoesNotExist:
        message = device + " DOESNT EXIST"
        return HttpResponse(message)



