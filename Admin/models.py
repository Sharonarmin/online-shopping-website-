from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class catagory_tb(models.Model):
    catagory = models.CharField(max_length=20)
