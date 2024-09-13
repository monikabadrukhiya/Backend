from django.shortcuts import render,redirect,HttpResponse
from signapp.models import Login

def Home(request):
    data=Login.objects.all()
    return render(request,"home.html",{'data':data})

def Adddata(request):
    if request.POST.get('submit')=='Submit':
        # id=request.POST.get('id')
        username=request.POST.get('username')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        re_Enterpassword=request.POST.get('re_Enterpassword')
    if(pwd==re_Enterpassword):
        Login.objects.create(username=username,email=email,password=pwd,re_Enterpassword=re_Enterpassword)
        return redirect("/") 
    else:
        message = "Passwords do not match"
        pwd=""
        re_Enterpassword=""
        return render(request, "home.html", {'message': message})
def loginclick(request):
    return render(request,'login.html') 

def Logindata(request):
    if request.POST.get('submit')=='Submit':
        lusername=request.POST.get('username')
        lpassword=request.POST.get('pwd')
        print("lname============",lusername)
        print("lpass==////////////////",lpassword),
    user=Login.objects.filter(username=lusername,password=lpassword).first()
    if user:
        return render(request,"success.html")
    else:
        return render(request,"login.html")

    


