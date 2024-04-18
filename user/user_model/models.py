from __future__ import unicode_literals
from django.db import models

class user_registration(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.email} {self.mobile} {self.password} {self.address}'