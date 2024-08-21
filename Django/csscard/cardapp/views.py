from django.shortcuts import render


def Home(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def Content(request):
    return render(request,"content.html")

def Pricing(request):
    return render(request,"pricing.html")

def kitchensing(request):
    return render(request,"kitchensink.html")

def Terms(request):
    return render(request,"terms.html")