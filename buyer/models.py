from django.db import models
from seller.models import *

# Create your models here.


class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class add_to_cart_tb(models.Model):
    product=models.ForeignKey(product_tb, on_delete=models.CASCADE)
    seller=models.ForeignKey(register_tb1, on_delete=models.CASCADE)
    address=models.CharField(max_length= 100)
    contact=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    total=models.CharField(max_length=20)
    buyer=models.ForeignKey(register_tb, on_delete=models.CASCADE ,default=1)

class order_tb(models.Model):
    product=models.ForeignKey(product_tb, on_delete=models.CASCADE)
    seller=models.ForeignKey(register_tb1, on_delete=models.CASCADE)
    address=models.CharField(max_length= 100)
    contact=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    total=models.CharField(max_length=20)
    buyer=models.ForeignKey(register_tb, on_delete=models.CASCADE ,default=1)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=20, default='none')

    

    
  
    
    
    
    
