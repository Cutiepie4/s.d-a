from __future__ import unicode_literals # must be first
from django.db import models

class ShipmentStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name
    
class Shipment(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    shipment_fee = models.IntegerField(default=40000)
    shipment_status_id = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.email} {self.mobile} {self.address} {self.shipment_fee} {self.shipment_status_id}'