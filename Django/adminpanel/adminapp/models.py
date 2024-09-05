from django.db import models

class superadmin(models.Model):
    username=models.CharField(max_length=20)