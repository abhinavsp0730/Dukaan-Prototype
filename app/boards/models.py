import math

from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    """
    model for saving vendors product data.
    """
    name = models.CharField(max_length=30, unique=True)
    details = models.CharField(max_length=4000)
    mrp = models.PositiveIntegerField() 
    discounted_price = models.PositiveIntegerField()
    available = models.BooleanField(default=True) 
    User = models.ForeignKey(User,on_delete = models.PROTECT, related_name='product_user')
    
    def __str__(self):
        return self.name


class Order(models.Model):
    """
    model for saving customers order data.
    """
    product_name = models.ForeignKey(Product, on_delete = models.PROTECT, related_name='order')
    name = models.CharField(max_length=30, unique=True)
    price = models.PositiveIntegerField() 
    qty = models.PositiveIntegerField()
    user_name = models.CharField(max_length=30)
    mob = models.CharField(max_length=30)
    adress = models.CharField(max_length=4000)
    user = models.ForeignKey(User,on_delete = models.PROTECT, related_name='product_order') 