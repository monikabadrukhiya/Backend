from django.db import models

class User(models.Model):
    userName=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)

    def __str__(self):
       return '{"userName":%s}' %(self.userName)