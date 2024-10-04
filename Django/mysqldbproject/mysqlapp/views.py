from django.shortcuts import render,redirect,HttpResponse
from mysqlapp.models import Databaseentry

def Home(request):
    data=Databaseentry.objects.all()
    return render(request,"signup.html",{'data':data})

def Signupdata(request):
    if request.POST.get('submit')=="Signup":
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        number=request.POST.get('num')
        print("id==========",id)
        print("user=============",fname)
        print("user=============",lname)
        print("email=============",email)
        print("pass=============",password)
        print("repass=============",number)
        if fname and lname and email and password and number:
            Databaseentry.objects.create(Firstname=fname,Lastname=lname,Email=email,Password=password,Number=number)
            return redirect("/")

# def Delete(request):