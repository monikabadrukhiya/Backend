from django.db import models
from userapp.models import User


    
class Education(models.Model):
    userName=models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)
    education=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)


    

