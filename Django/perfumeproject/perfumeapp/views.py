from django.shortcuts import render,redirect
from adminpanelapp .models import *
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)


def Home(request):
    # category_data = Category.objects.all()
    product_data=Products.objects.all()
    return render(request,"index.html",{"product_data":product_data })

def categories_processor(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'categories': categories}

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login_data(request):
      if request.POST.get('submit')=="Submit":
        luser=request.POST.get('name')
        lpassword=request.POST.get('pswd')
        
        if luser and lpassword:
            userid=Users.objects.filter(user_name=luser,user_password=lpassword).first()
            if userid:
                userid=request.session['member']=userid.id
                return redirect("/")
            else:
             return render(request,"login.html")
      return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)          
def Ragister_data(request):
     if request.POST.get('submit')=="Submit":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pswd')
        number=request.POST.get('num')

        if username and email and password and number:
            Users.objects.create(user_name=username,user_email=email,user_password=password,user_number=number)
            return redirect("/")
     return render(request,"signup.html")

def Logout(request):
    del request.session['member']
    productid=request.GET.get("productid")
    Products.objects.filter(id=productid).delete()
    return redirect("/")


def categorywisedata(request):
    categoryid=request.GET.get("categoryid")
    categorywise_product=Products.objects.filter(category_id=categoryid)
    
    return render(request,"categorywise.html",{"categorywise_product":categorywise_product})

def shopdata(request):
    all_product=Products.objects.all()
    
    return render(request,"shop.html",{"all_product":all_product})


def About(request):
    return render(request,"aboutus.html")

def Contactdata(request):
    if request.POST.get('submit')=="Submit":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        if name and email and message:
            Contact.objects.create(contact_name=name,contact_email=email,message=message)
    return render(request,"contact.html")

def Quantity(request):
    item=request.GET.get("itemid")
    action=request.GET.get("actionid")
    cart_item=Cartdata.objects.get(id=item)
    if action=="increase":
        cart_item.quantity=int(cart_item.quantity)+1
    elif action=="decrease":
        cart_item.quantity=int(cart_item.quantity)-1
    cart_item.save()
    return redirect("cartdata")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Cart(request):
    productid=request.GET.get("productid")
    print("productid==========",productid)
    userid=request.session.get('member')
    if userid==None:
        return render(request,"login.html") 
    else:
        c_user=Users.objects.get(id=userid)
        c_product=Products.objects.get(id=productid)

        Cartdata.objects.create(userid = c_user,product_id=c_product)
        return redirect("/cartdata")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Cart_data(request):
    userid=request.session.get('member')

    if userid==None:
        return render(request,"login.html")
    else:
        cart_data=Cartdata.objects.filter(userid=userid)
        sum=0
        for i in cart_data:
            total= i.quantity * int(i.product_id.product_price)
            Cartdata.objects.filter(id=i.id).update(total=total)
            sum=sum+total
        cart_data=Cartdata.objects.filter(userid=userid)
        return render(request,"cart.html",{'cart_data':cart_data,'grand_total':sum})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def Delete_cartdata(request):
    delete_cartid=request.GET.get("deleteid")
    if delete_cartid and int(delete_cartid)>0:
        Cartdata.objects.filter(id=int(delete_cartid)).delete()
    return redirect("/cartdata")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Discription(request):
    productid=request.GET.get("productid")
    discription_data=Products.objects.get(id=productid)
    return render(request,"discription.html",{'discription_data':discription_data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def cheoutdata(request):
    cart_data=Cartdata.objects.all()
    sum=0
    for i in cart_data:
            total= i.quantity * int(i.product_id.product_price)
            Cartdata.objects.filter(id=i.id).update(total=total)
            sum=sum+total

    return render(request,"checkout.html",{'cart_data':cart_data,'grand_total':sum})
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Checkout(request):
    userid=request.session.get('member')
    c_user=Users.objects.get(id=userid)
    
    cart_data=Cartdata.objects.filter(userid=userid)
    sum=0
    ids = []
    for i in cart_data:
            total= i.quantity * int(i.product_id.product_price)
            sum=sum+total
            ids.append(str(i.product_id.pk))

            select_p=Products.objects.get(id=i.product_id.pk)
            update_qty=select_p.available_qty-i.quantity
            select_p.available_qty=update_qty
            select_p.save()
    str_ids =','.join(ids)

    c_state=request.POST.get("c_state")
    c_fname=request.POST.get("c_fname")
    c_lname=request.POST.get("c_lname")
    c_address=request.POST.get("c_address")
    c_city=request.POST.get("c_city")
    c_zip=request.POST.get("c_zip")
    c_email=request.POST.get("c_email")
    c_phone=request.POST.get("c_phone")
             
    Order.objects.create(userid=c_user,product_ids=str_ids,customer_fname=c_fname,customer_lname=c_lname,customer_address=c_address,city=c_city,country=c_state,pincode=c_zip,email=c_email,number=c_phone,total_amount=sum)
    Cartdata.objects.filter(userid=userid).delete()
    return redirect("thankyou")

def Thankyou(request):
    return render(request,"thankyou.html")

