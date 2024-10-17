from django.db import models

class Category(models.Model):
    categoryName=models.CharField(max_length=100)
    categoryimg=models.ImageField( upload_to="image/")

    def __str__(self):
       return '{"categoryName":%s}' %(self.categoryName)
    