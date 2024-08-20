from django.db import models

class Login(models.Model):
    Name=models.CharField(max_length=20)
    ContactNo=models.IntegerField(max_length=12)
    Gender=models.CharField(max_length=10)
    Hobby=models.CharField(max_length=50)
    City=models.CharField(max_length=20)
