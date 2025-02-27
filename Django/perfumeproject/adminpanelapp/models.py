from django.db import models
import os

class SuperAdmin(models.Model):
    name=models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)

class Users(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField( max_length=254)
    user_password=models.CharField( max_length=200)
    user_number = models.IntegerField()

class Category(models.Model):
    category_name = models.CharField(max_length=200)

class Products(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField( max_length=200)
    product_price = models.FloatField()
    product_image = models.FileField( upload_to='image/')
    product_discription=models.TextField()
    available_qty=models.IntegerField()
    
class Cartdata(models.Model):
    userid=models.ForeignKey(Users,  on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,  on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total=models.IntegerField(default=0)

class Order(models.Model):
    userid=models.ForeignKey(Users,  on_delete=models.CASCADE)
    product_ids = models.TextField()
    customer_fname=models.CharField( max_length=50)
    customer_lname=models.CharField( max_length=50)
    customer_address=models.TextField()
    country=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    pincode=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    number=models.IntegerField()
    total_amount=models.FloatField()
    status=models.IntegerField(default=0)

class Contact(models.Model):
    contact_name=models.CharField( max_length=100)
    contact_email=models.EmailField( max_length=254)
    message=models.TextField()