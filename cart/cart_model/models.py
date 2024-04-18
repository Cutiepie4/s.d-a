from django.db import models
from django.urls import reverse

class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user_id} {self.product_id} {self.product_quantity}'
