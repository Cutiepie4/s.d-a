from djongo import models

class ClothesCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.category_name}'

class Clothes(models.Model):
    pid = models.CharField(max_length=255)
    category = models.IntegerField()
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    meta_keyword = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pid} {self.category} {self.name} {self.brand} {self.image_url} {self.description} {self.quantity} {self.price} {self.meta_keyword}"