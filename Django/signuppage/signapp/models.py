from django.db import models

class Login(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    re_Enterpassword=models.CharField(max_length=20)
