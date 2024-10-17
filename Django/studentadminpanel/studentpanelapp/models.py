from django.db import models

class Signdata(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField( max_length=254)
    Username=models.CharField( max_length=50)
    Password=models.CharField( max_length=50)

class Admission(models.Model):
    Name=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=20)
    Pnumber=models.IntegerField(max_length=20)
    Study=models.CharField(max_length=50)
    Cource=models.CharField(max_length=50)
    Fees=models.CharField(max_length=50)
    Duration=models.CharField(max_length=50)
    Joindate=models.CharField(max_length=12)
    Reference=models.CharField(max_length=50)
    Photo=models. ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)


class Inquiry(models.Model):
    Name=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=20)
    Pnumber=models.IntegerField(max_length=20) 
    Study=models.CharField(max_length=50)
    Reference=models.CharField(max_length=50)
    Inquiry=models.CharField(max_length=50)
    Status=models.CharField(max_length=20)
    expectedDate=models.DateTimeField()
    visitedDate=models.DateTimeField()  