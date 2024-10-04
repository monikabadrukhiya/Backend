from django.shortcuts import render,redirect,HttpResponse
from sessionapp.models import Login
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(request):
    return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Signupdata(request):
    if request.POST.get('submit')=="Signup":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        repassword=request.POST.get('re-pswd')
        print("user=============",username)
        print("email=============",email)
        print("pass=============",password)
        print("repass=============",repassword)
        if password and repassword:
            Login.objects.create(Username=username,Email=email,Password=password,Re_password=repassword)
            return render(request,"login.html")
        else:
            msg="Password do not match"
            return render(request,"signup.html",msg)
    return render(request,"signup.html")
        
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def signup(request):
#     return render(request,"signup.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logindata(request):
     if request.POST.get('submit')=="login":
        luser=request.POST.get('username')
        lpass=request.POST.get('pswd')

        print("user=============",luser)
        print("pass=============",lpass)

        if luser and lpass:
            user=Login.objects.filter(Username=luser,Password=lpass).first()
            if user:
                id=request.session['member']=user.id
                print("id==========",id)
                return redirect("/check")
            else:
                return HttpResponse("Invalid Username or Password")
        else:
            return HttpResponse("Please add username and password")
        
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Checking(request):
    data=request.session.get('member')
    print("data id : ",data)
    if data==None:
        return redirect("/")
    else:
        content={
            'data':data
        }
        return render(request,"logout.html",content)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Deleteid(request):
    try:
      data=request.session.get('member')
      del request.session['member']
      return redirect("/")
    except:
        return redirect("/check")
        

        