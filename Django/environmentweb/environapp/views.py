from django.shortcuts import render,redirect

def Home(request):
    return render(request,"index.html")

def Erroe404(request):    
    return render(request,"404.html")

def About(request):
    return render(request,"about.html")

def Blog(request):
    return render(request,"blog.html")

def Causes(request):
    return render(request,"causes.html")

def Contact(request):
    return render(request,"contact.html")

def Donation(request):
    return render(request,"donation.html")

def Event(request):
    return render(request,"events.html")

def Gallary(request):
    return render(request,"gallery.html")

def Service(request):
    return render(request,"service.html")

def Volunteer(request):
    return render(request,"volunteer.html")