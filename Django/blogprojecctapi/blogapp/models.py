from django.db import models
from userapp.models import User
from catagoryapp.models import Category

class Blog(models.Model):
    userName=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    categoryName=models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blogimage=models.ImageField( upload_to="image/")
    blogtitle=models.CharField( max_length=100)
    description=models.CharField(max_length=200)

    def __str__(self):
       return '{"blogtitle  ":%s}' %(self.blogtitle)

class Comment(models.Model):
     userid=models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
     blogid=models.ForeignKey(Blog, related_name='blogusers', on_delete=models.CASCADE)
     comment=models.CharField(max_length=200)
     date=models.DateField( auto_now=True, auto_now_add=False)
     
