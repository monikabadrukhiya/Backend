from django.shortcuts import render,redirect,HttpResponse
from sessionexamapp.models import Login

def Home(request):
    return render(request,"login.html")

def Signupdata(request):
    if request.POST.get('submit')=="Sumbit":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        numbeer=request.POST.get('num')

        print("username========",username)
        print("username========",email)
        print("username========",password)
        print("username========",numbeer)

        if username and password and email and numbeer:
            Login.objects.create(Username=username,Email=email,Password=password,Number=numbeer)
            return redirect("/")
        else:
                return render(request,"signup.html")    
    return render(request,"signup.html")    

def Logindata(request):
       if request.POST.get('submit')=="Sumbit":
        luser=request.POST.get('name')
        lpass=request.POST.get('pswd')

        print("luser======",luser)
        print("luser======",lpass)

        if  luser and lpass:
             user=Login.objects.filter(Username=luser,Password=lpass).first()
             if user:
                id=request.session['member']=user.id
                print("id====",id)
                return redirect("/check")
             else:
                return redirect("/")
        
def Checking(request):
     dataid=request.session.get('member')
     print(dataid)

     if dataid == None:
         return redirect("/")
     else:
        content={
            'data':dataid

        }
        return render(request,"logout.html",content)

def Delete(request):
    try:
        del request.session['member']
        return redirect("/")
    except:
        return redirect("/check")
    
def Aboutus(request):
    return render(request,"aboutus.html")
