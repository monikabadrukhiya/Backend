from django.db import models

class Dataentry(models.Model):
    Photo=models.ImageField(upload_to='image/')
    Product=models.CharField(max_length=20)
    Price=models.CharField(max_length=10)
    
class Indexblog(models.Model):
    Photo=models.ImageField(upload_to='image/')
    Title=models.CharField(max_length=50)
    Name=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)

class UserEnter(models.Model):
    Email=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)

class Shopdata(models.Model):
    Photo=models.ImageField(upload_to='image/')
    Title=models.CharField(max_length=50)
    Price=models.IntegerField(max_length=10)

class Aboutdata(models.Model):
    Photo=models.ImageField(upload_to='image/')
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Description=models.CharField(max_length=200)
    LM=models.CharField(max_length=200)

class Servicesdata(models.Model):
    FName=models.CharField(max_length=50)
    LName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Message=models.CharField(max_length=200)

class Cart(models.Model):
    Photo=models.ImageField(upload_to='image/')
    Product=models.CharField(max_length=20)
    Price=models.IntegerField(max_length=10)
    Quantity=models.IntegerField(default=1)
    Total=models.IntegerField(default=0)


class Checkout(models.Model):
    Country =models.CharField(max_length=20)
    FName=models.CharField(max_length=50)
    LName=models.CharField(max_length=50)
    Company=models.CharField(max_length=50)
    Address =models.CharField(max_length=50)
    State  =models.CharField(max_length=50)
    Zip=models.IntegerField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone =models.IntegerField(max_length=50)
    Note=models.CharField(max_length=200)
    CouponCode =models.IntegerField(max_length=50)
    Password=models.CharField(max_length=20)


class Login(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=15)







    


