from django.db import models

class Login(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Re_password=models.CharField(max_length=50)