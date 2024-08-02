from django.db import models

class Login(models.Model):
    name=models.CharField(max_length=20)
    maths=models.IntegerField(max_length=20)
    sci=models.IntegerField(max_length=20)
    phy=models.IntegerField(max_length=20)
    total=models.IntegerField(max_length=20)
    per=models.IntegerField(max_length=20)
