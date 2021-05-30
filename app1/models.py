from django.db import models
from Product.models import Product
# Create your models here.

class orderform(models.Model):
    customer = models.CharField(max_length=20)
    Product = models.ForeignKey("Product.Product",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
