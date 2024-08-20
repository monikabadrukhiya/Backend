from django.db import models

class Login(models.Model):
    name=models.CharField(max_length=20)
    maths=models.CharField(max_length=20)
    sci=models.CharField(max_length=20)
    phy=models.CharField(max_length=20)
    total=models.CharField(max_length=20)
    per=models.CharField(max_length=20)
