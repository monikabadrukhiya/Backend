from django.db import models
from userapp.models import User


class Result(models.Model):
    userName=models.ForeignKey(User, related_name='result', on_delete=models.CASCADE)
    science=models.IntegerField()
    physics=models.IntegerField()
    maths=models.IntegerField()
    
    

