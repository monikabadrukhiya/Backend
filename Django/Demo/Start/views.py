from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("this is my home page")

def about(request):
    return HttpResponse("this is my admin page")

