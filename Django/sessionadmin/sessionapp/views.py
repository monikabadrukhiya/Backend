from django.shortcuts import render,redirect,HttpResponse
from sessionapp.models import Login
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(Request):
    return render(Request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
            return render(request,"/")
        else:
            msg="Passwords do not match"
            password=""
            re_password=""
            return render(request,"signup.html",{'msg':msg})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signdata(request):
    return render(request,"signup.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logindata(request):
    if request.GET.get('submit')=="Submit":
        luser=request.GET.get('username')
        lpwd=request.GET.get('pswd')
        print("luser======",luser)
        print("luser======",lpwd)
    if luser and lpwd :
        user=Login.objects.filter(Username=luser,Password=lpwd).first()
        print("user//////////",user)
        if user:
            id= request.session["member"]=user.id
            print("id==============",id)
            return redirect("/check")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return HttpResponse("Please provide both Username and Password")
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Checking(request):
    data=request.session.get('member')
    if data==None:
        return redirect('/')
    else:
        content={
            "data":data
        }
        return render(request,"logout.html",content)
    
def deleteid(request):
    data=request.session['member']
    try: 
        data=request.session['member']
        del request.session['member']
        return redirect("/")
    except:
         return redirect("check")
    



    

