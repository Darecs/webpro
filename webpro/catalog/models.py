from django.db import models

# Create your models here.
class DeviceList(models.Model):
    device_type = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=15)
