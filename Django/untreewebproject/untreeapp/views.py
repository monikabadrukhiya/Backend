from django.shortcuts import render,redirect
from untreeapp.models import Dataentry,Indexblog,UserEnter,Shopdata,Aboutdata,Servicesdata
def Home(request):
    indexdata=Dataentry.objects.all()
    iblogdata=Indexblog.objects.all()
    userentry=UserEnter.objects.all()
    return render(request,"index.html",{'indexdata':indexdata,'iblogdata':iblogdata,'userentry':userentry})

def Add(request):
    name=request.GET.get('name')
    email=request.GET.get('email')
    if name and email:
        UserEnter.objects.create(Name=name,Email=email)
    return redirect("/")


def About(request):
    aboutdata=Aboutdata.objects.all()
    return render(request,"about.html",{'aboutdata':aboutdata})

def Blog(request):
    iblogdata=Indexblog.objects.all()
    return render(request,"blog.html",{'iblogdata':iblogdata})

def Cart(request):
    return render(request,"cart.html")

def Checkout(request):
    return render(request,"checkout.html")

def Contact(request):
    cdata=Servicesdata.objects.all()
    print("sdata=========",cdata)
    return render(request,"contact.html",{'cdata':cdata})


def Contactdata(request):
        # if request.GET.get('submit')=='Submit':
            fname=request.GET.get('fname')
            print("fname=========",fname)
            lname=request.GET.get('lname')
            email=request.GET.get('email')
            msg=request.GET.get('message')
            if fname and email and lname and msg:
                Servicesdata.objects.create(FName=fname,Email=email,LName=lname,Message=msg)
            return redirect("/contact")

def Service(request):
    indexdata=Dataentry.objects.all()
    return render(request,"services.html",{'indexdata':indexdata})

def Shop(request):
    shopdata=Shopdata.objects.all()
    return render(request,"shop.html",{'shopdata':shopdata})

def Thankyou(request):
    return render(request,"thankyou.html")