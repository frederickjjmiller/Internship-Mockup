from django.db import models

# Create your models here.


class Device(models.Model):

    # These are the various fields that are filled by the API calls
    # Device Information Fields
    asset_tag = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, default='Unknown')
    ip_address = models.CharField(max_length=45, default='127.0.0.1')
    vendor = models.CharField(max_length=100, default='Unknown')
    serial_number = models.CharField(max_length=100, default='Unknown')
    is_wireless = models.BooleanField(default=True)

    # Device Location Fields - Should be inferred from Access Point / Switch naming convention
    building_address = models.CharField(max_length=100, default='None')
    building_name = models.CharField(max_length=100, default='None')
    building_floor = models.CharField(max_length=100, default='None')

    # Wireless AP Connection Information - Queried from Airwave API
    access_point = models.CharField(max_length=100, default='None')
    connection_time = models.CharField(max_length=100, default="Unknown")
    signal_strength = models.CharField(max_length=100, default="Unknown")
    second_ap = models.CharField(max_length=100, default='Unknown')
    third_ap = models.CharField(max_length=100, default='Unknown')
    fourth_ap = models.CharField(max_length=100, default='Unknown')
    fifth_ap = models.CharField(max_length=100, default='Unknown')
    sixth_ap = models.CharField(max_length=100, default='Unknown')

    # Wired Switch Connection Information - Queried from Netdisco DB
    switch = models.CharField(max_length=100, default="Unknown")
    switch_location = models.CharField(max_length=100, default="Unknown")
    switch_port = models.IntegerField(default=0)
    last_seen = models.CharField(max_length=100, default="Unknown")
    first_discovered = models.CharField(max_length=100, default="Unknown")

    # Device User Information - Queried from ServiceNow
    assigned_user = models.CharField(max_length=100, default='None')
    last_login_user = models.CharField(max_length=100, default='None')
    last_login_date = models.CharField(max_length=100, default="Unknown")

    objects = models.Manager()

    def __str__(self):
        return self.asset_tag



