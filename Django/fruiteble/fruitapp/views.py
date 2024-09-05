from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def Error(request):
    return render(request,"404.html")

def Cart(request):
    return render(request,"cart.html")

def Chackout(request):
    return render(request,"chackout.html")

def Contact(request):
    return render(request,"contact.html")

def Shopdetail(request):
    return render(request,"shop-detail.html")

def Shop(request):
    return render(request,"shop.html")

def Testimonial(request):
    return render(request,"testimonial.html")