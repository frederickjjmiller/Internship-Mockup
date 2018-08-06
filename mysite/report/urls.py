from django.urls import path

from . import views

urlpatterns = [
    # ex: /report/
    path('', views.get_device, name='Device Lookup Page'),
    path('device/<str:device>/', views.device_report, name='Device Report'),
    path('address/<str:address>/', views.ip_report, name='Device Report'),
    path('serial/<str:serial>/', views.serial_report, name='Device Report')
]
