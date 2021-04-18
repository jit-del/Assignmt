
from django.db import models

# Create your models here.


class Admin(models.Model):
    name=models.CharField(max_length=20,unique=True)
    dob=models.DateField()
    phone=models.IntegerField()
    password=models.CharField(max_length=10)
    image=models.ImageField(upload_to='user/image')

class User(models.Model):
    name=models.CharField(max_length=20,unique=True)
    dob=models.DateField()
    phone=models.IntegerField()
    password=models.CharField(max_length=10)
    image=models.ImageField(upload_to='admin/image')
    mark=models.IntegerField()