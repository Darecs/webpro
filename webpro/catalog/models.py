from django.db import models

class dna_center(models.Model):
    hostname = models.CharField(max_length = 30)
    ip_address= models.IPAddressField
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 30)

