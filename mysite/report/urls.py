from django.urls import path

from . import views

urlpatterns = [
    # ex: /report/
    path('', views.get_device, name='Device Lookup Page'),
    path('device/<str:device>/', views.device_report, name='Device Report'),
]