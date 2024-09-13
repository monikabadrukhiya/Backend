from django.shortcuts import render,redirect,HttpResponse
from sessionapp.models import Login

def Home(Request):
    data=Login.objects.all()
    return render(Request,"signup.html",{'data':data})

def Adddata(request):
    if request.GET.get('submit')=="Submit":
        id=request.GET.get('id')
        username=request.GET.get('username')
        email=request.GET.get('email')
        password=request.GET.get('pswd')
        re_password=request.GET.get('re-pswd')
        print("id===",id)
        print("id===",username)
        if(password==re_password):
            Login.objects.create(Username=username,Email=email,Password=password,Reenterpassword=re_password)
            return redirect("/")
        else:
            msg="Passwords do not match"
            password=""
            re_password=""
            return render(request,"signup.html",{'msg':msg})

        
def loginclick(request):
    return render(request,"login.html")

def Logindata(request):
    if request.GET.get('submit')=="Submit":
        luser=request.GET.get('Username')
        lpwd=request.GET.get('pswd')
        print("luser======",luser)
        print("luser======",lpwd)

    user=Login.objects.filter(Username=luser,Password=lpwd).first()
    print("user//////////",user)
    if user:
        data=Login.objects.all()
        userdata=Login.objects.filter(Username=luser,Password=lpwd).first()
        return render(request,"logout.html",{'userdata':userdata})
    else:
        return render(request,"login.html")

    

