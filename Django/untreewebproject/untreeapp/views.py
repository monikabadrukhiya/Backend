from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

from untreeapp.models import Dataentry,Indexblog,UserEnter,Shopdata,Aboutdata,Servicesdata,Cart,Checkout,Login
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(request):
    indexdata=Dataentry.objects.all()
    iblogdata=Indexblog.objects.all()
    userentry=UserEnter.objects.all()
    return render(request,"index.html",{'indexdata':indexdata,'iblogdata':iblogdata,'userentry':userentry})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Add(request):
    name=request.GET.get('name')
    email=request.GET.get('email')
    if name and email:
        UserEnter.objects.create(Name=name,Email=email)
    return redirect("/")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def About(request):
    aboutdata=Aboutdata.objects.all()
    return render(request,"about.html",{'aboutdata':aboutdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Blog(request):
    iblogdata=Indexblog.objects.all()
    return render(request,"blog.html",{'iblogdata':iblogdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Cartt(request):
    id=request.GET.get('getid')
    sid=Shopdata.objects.filter(id=id).first()
    sPhoto=sid.Photo
    sProduct=sid.Title 
    sprice=sid.Price
    
    Cart.objects.create(Photo=sPhoto,Product=sProduct,Price=sprice)
    return redirect("/data")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Cartdata(request):
    dataid=request.session.get('member')
    print("dataid.............",dataid)
    
    if dataid == None:
        return render(request,"login.html")
    else:

        cartdata=Cart.objects.all()
        sum=0
        for i in cartdata:
            total=i.Quantity * int(i.Price)
            Cart.objects.filter(id=i.id).update(Total=total)
            sum=sum+total

        cartdata=Cart.objects.all()
        return render(request,"cart.html",{"cdata":cartdata,"grand_total":sum})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Delete(request):
     id=request.GET.get('deleteid')

     if (id and int(id)>0):
          Cart.objects.get(id=int(id)).delete()
          return redirect("/data")
     
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Checkoutt(request):
     checkdata=Checkout.objects.all()
     cartdata=Cart.objects.all()
     sum=0
     for i in cartdata:
        total=i.Quantity * int(i.Price)
        sum=sum+total
     return render(request,"checkout.html",{"checkdata":checkdata,"cartdata":cartdata,"grand_total":sum})
     
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Checkoudata(request):
    country=request.GET.get('c_city')
    fname=request.GET.get('c_fname')
    lname=request.GET.get('c_lname')
    company=request.GET.get('c_company')
    address=request.GET.get('c_address')
    state=request.GET.get('c_state')
    zip=request.GET.get('c_zip')
    email=request.GET.get('c_email')
    phone=request.GET.get('c_phone')
    password=request.GET.get('c_password')
    note=request.GET.get('note')
    code=request.GET.get('c_code')

    Checkout.objects.create(Country=country,FName=fname,LName=lname,Company=company,Address=address,State=state
    ,Zip=zip,Email=email,Phone=phone,Note=note,CouponCode=code,Password=password)
    return redirect("/thankyou")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Contact(request):
    cdata=Servicesdata.objects.all()
    print("sdata=========",cdata)
    return render(request,"contact.html",{'cdata':cdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Service(request):
    indexdata=Dataentry.objects.all()
    return render(request,"services.html",{'indexdata':indexdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Shop(request):
    shopdata=Shopdata.objects.all() 
    return render(request,"shop.html",{'shopdata':shopdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Thankyou(request):
    return render(request,"thankyou.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Signupdata(request):
     if request.POST.get('submit')=="Signup":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        number=request.POST.get('num')
        print("user=============",username)
        print("email=============",email)
        print("pass=============",password)
        print("repass=============",number)
        if username and email and password and number :
            Login.objects.create(Username=username,Email=email,Password=password,Number=number)
            return redirect("/logindata")
    
     return render(request,"signup.html")


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
                return redirect("/data")
        
     return render(request,"login.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Deletelogindata(request):
    try:
        del request.session['member']
        return redirect("/")
    except:
        return redirect("/data")
    
def Adminpanel(request):
    return render(request,"admin.html")
