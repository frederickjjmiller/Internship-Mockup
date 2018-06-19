from django.db import models

# Create your models here.


class Device(models.Model):
    asset_tag = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, default='Unknown')
    ip_address = models.CharField(max_length=45, default='127.0.0.1')
    building_address = models.CharField(max_length=100, default='None')
    building_name = models.CharField(max_length=100, default='None')
    building_floor = models.CharField(max_length=100, default='None')
    access_point = models.CharField(max_length=100, default='None')
    signal_strength = models.IntegerField(default=0)
    assigned_user = models.CharField(max_length=100, default='None')
    last_login_user = models.CharField(max_length=100, default='None')
    last_login_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.asset_tag
