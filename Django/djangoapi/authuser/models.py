from django.db import models

class authusermodel(models.Model):
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=100)