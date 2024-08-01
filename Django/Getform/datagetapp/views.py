from django.shortcuts import render

def Home(request):
    return render(request,"home.html")

def Dataget(request):
    Name=request.GET.get('name')
    print('n=',Name)
    Email=request.GET.get('Email')
    Password=request.GET.get('password')
    Number=request.GET.get('number')
    Gender=request.GET.get('Gender')

    data={
        'Name':Name,
        'Email':Email,
        'Password':Password,
        'Number':Number,
        'Gender':Gender
        
    }
    return render(request,"home.html",data)



