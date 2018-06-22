from django.db import models

# Create your models here.


class Device(models.Model):

    # These are the various fields that are filled by the API calls
    # Device Information Fields
    asset_tag = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, default='Unknown')
    ip_address = models.CharField(max_length=45, default='127.0.0.1')
    vendor = models.CharField(max_length=100, default='Unknown')

    # Device Location Fields
    building_address = models.CharField(max_length=100, default='None')
    building_name = models.CharField(max_length=100, default='None')
    building_floor = models.CharField(max_length=100, default='None')

    # Device Connection Information
    access_point = models.CharField(max_length=100, default='None')
    connection_time = models.IntegerField(default=0)
    signal_strength = models.IntegerField(default=0)
    last_five_access_points = models.CharField(max_length=200, default='None, None, None, None, None')

    # Device User Information
    assigned_user = models.CharField(max_length=100, default='None')
    last_login_user = models.CharField(max_length=100, default='None')
    last_login_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.asset_tag
