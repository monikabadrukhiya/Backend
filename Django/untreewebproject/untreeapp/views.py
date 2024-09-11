from django.shortcuts import render,redirect
from untreeapp.models import Dataentry,Indexblog,UserEnter,Shopdata,Aboutdata,Servicesdata,Cart
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

def Cartt(request):
    cartdata=Cart.objects.all()

    id=request.GET.get('getid')
    # quantity = request.GET.get('quantity', 1)
    sid=Shopdata.objects.filter(id=id).first()
    sPhoto=sid.Photo
    sProduct=sid.Title 
    sprice=sid.Price
    
    
    Cart.objects.create(Photo=sPhoto,Product=sProduct,Price=sprice)
    return redirect("/data")

def Cartdata(request):
    cartdata=Cart.objects.all()
    sum=0
    for i in cartdata:
        total=i.Quantity * int(i.Price)
        Cart.objects.filter(id=i.id).update(Total=total)
        sum=sum+total

    cartdata=Cart.objects.all()
    return render(request,"cart.html",{"cdata":cartdata,"grand_total":sum})

def Quantitty(request):
     item=request.GET.get("itemid")
     action=request.GET.get("actionid")
     cart_item=Cart.objects.get(id=item)
     if action=="increase":
          cart_item.Quantity = int(cart_item.Quantity) + 1
     elif action=="decrease":
          cart_item.Quantity  = int(cart_item.Quantity) - 1
     cart_item.save()
    
     return redirect("/data")


def Delete(request):
     id=request.GET.get('deleteid')

     if (id and int(id)>0):
          Cart.objects.get(id=int(id)).delete()
          return redirect("/data")
     

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