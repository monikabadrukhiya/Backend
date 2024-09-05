from django.shortcuts import render

def Home(request):
    return render(request,"index.html")

def About(request):
    return render(request,"about.html")

def Appoinment(request):
    return render(request,"appoinment.html")

def Blogsidebar(request):
    return render(request,"blog-sidebar.html")

def Blogsingle(request):
    return render(request,"blog-single.html")

def Confirmation(request):
    return render(request,"confirmation.html")

def Contact(request):
    return render(request,"contact.html")

def Departmentsingle(request):
    return render(request,"department-single.html")

def Department(request):
    return render(request,"department.html")

def Doctorsingle(request):
    return render(request,"doctor-single.html")

def Doctor(request):
    return render(request,"doctor.html")

def Documentation(request):
    return render(request,"documentation.html")

def Service(request):
    return render(request,"service.html")