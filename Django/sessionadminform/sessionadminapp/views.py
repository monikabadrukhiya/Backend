from django.shortcuts import render,redirect,HttpResponse
from sessionadminapp.models import Login

def Home(request):
    return render(request,"login.html")

def Signdata(request):
    if request.POST.get('submit')=="Submit":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        number=request.POST.get('num')

        print("user==",username)
        print("user==",email)
        print("user==",password)
        print("user==",number)
        if username and email and password and number:
            Login.objects.create(Username=username,Email=email,Password=password,Number=number)
            return redirect("/")
        else:
            return render(request,"signup.html")
    return render(request,"signup.html")

def Logindata(request):
     if request.POST.get('submit')=="Submit":
        luser=request.POST.get('name')
        lpassword=request.POST.get('pswd')

        if luser and lpassword:
            user=Login.objects.filter(Username=luser,Password=lpassword).first()
            if user:
                id=request.session['member']=user.id
                print("id========",id)
                return redirect("/check")
            else:
                return redirect("/")
            
def Checking(request):
    userid=request.session.get('member')
    print("userid=======",userid)

    if userid == None:
        return redirect("/")
    else:
        content={
        'data':userid
        }
        return render(request,"logout.html",content)

def Deleteid(request):
     try:
          userid=request.session.get('member')
          print("userid=======",userid)
          del request.session['member']
          return redirect("/")
     except:
         return render(request,"/check")

    


    


    