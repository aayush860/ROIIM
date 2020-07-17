from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class configuration_key(models.Model):
    api_key = models.TextField()

class user_details(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.TextField()
    phone = models.CharField(max_length=10)
    dob = models.TextField()

class billing_details(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=16)
    street = models.TextField()
    street2 = models.TextField()
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=8)
    country = models.CharField(max_length=32)
    state = models.CharField(max_length=32)