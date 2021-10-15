from django.db import models
from Admin.models import *
from buyer.models import *

# Create your models here.

class register_tb1(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    country=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')

class product_tb(models.Model):
    file=models.FileField(default='no pic')
    seller=models.ForeignKey(register_tb1,on_delete=models.CASCADE, default=9)
    product=models.CharField(max_length=20)
    details=models.CharField(max_length=50)
    catagory=models.ForeignKey(catagory_tb, on_delete=models.CASCADE)
    stock=models.CharField(max_length=20)
    price=models.IntegerField()

class trackingDetails(models.Model):
    product=models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE)
    place=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
