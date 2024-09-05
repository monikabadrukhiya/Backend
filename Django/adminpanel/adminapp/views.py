from django.shortcuts import render,redirect
from adminapp.models import superadmin

def Home(request):
    data=superadmin.objects.all()
    return render(request,"index.html",{'data':data})