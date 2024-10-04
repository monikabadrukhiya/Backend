from django.db import models

class Login(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=50)
