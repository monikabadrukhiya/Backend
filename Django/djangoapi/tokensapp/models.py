from django.db import models
from django.contrib.auth.models import AbstractUser

class Tokenmodel(AbstractUser):
    phone=models.CharField(max_length=30)
   