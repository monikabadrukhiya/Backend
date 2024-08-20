from django.db import models

class Form(models.Model):
    Header=models.CharField(max_length=200)
    Disctiption=models.CharField(max_length=200)
    Readmore=models.CharField(max_length=200)
    footer=models.CharField(max_length=200)
