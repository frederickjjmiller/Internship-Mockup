# device_lookup.py
# Author: Frederick J. Miller
# Purpose: A series of functions to take input, examine a .csv, and make database calls associated with looking up
# a network device

from django.core.exceptions import ObjectDoesNotExist

from .models import NetDevice

import csv
from .netdisco_models import Device, DevicePort

def servicenow_lookup(search, parameter):

    # Search the ServiceNow .CSV file for the correct device based on search criteria, and save relevant information
    # to the default database
    # search is the text entry field, parameter is the selection from asset_tag, serial_number, or ip_address

    with open('service_now.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #find out which row[i] == parameter
                line_count += 1
            else:
                # check if the search term matches
                if row[] == search:
                    # Check if the network device is in the database
                    try:
                        # query = NetDevice.objects.get(mac_address=mac)
                        # Store the contents in the database
                    except ObjectDoesNotExist:
                        # Create a new object in the database
                        # query = NetDevice.create(mac)
                        # Store the contents in the database
                        # Then return the mac address so we can lookup with other services
                        return mac
    # IF we get to this, this means there was an error looking up the device
    return 1


def netdisco_lookup(mac):

    # Search the NetDisco Database for device information on the given mac address and store relevant information in
    # the default database
    try:
        query = DevicePort.objects.get(mac=mac)
        # Pull relevant data from netdisco database and store in appdata db
    except ObjectDoesNotExist:
        # Some exception since it's not in netdisco for some reason.


def device_lookup(search):

    # The primary function. Combines all lookups and API calls to discover a device.

    mac = servicenow_lookup(search)
    netdisco_lookup(mac)
    # The Airwave API call goes here
    # If Airwave returns error, device is wired.
    # Otherwise we should flag as wireless.