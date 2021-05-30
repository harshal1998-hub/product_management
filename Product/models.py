from django.db import models

# Create your models here.
class Product(models.Model):
    Product_name = models.CharField(max_length = 150)
    price = models.IntegerField(default=0)
    Qty = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
