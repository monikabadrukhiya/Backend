from django.db import models

class User(models.Model):
    userName=models.CharField(max_length=20)
    email=models.EmailField( max_length=254)
    password=models.CharField(max_length= 20)
    

    def __str__(self):
        return '{"name":%s}' % (self.userName)
    
    

