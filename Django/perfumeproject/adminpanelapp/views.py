from django.shortcuts import render,redirect,HttpResponse
from adminpanelapp .models import *
from django.views.decorators.cache import cache_control
import os
# from datetime import date

# today = date.today()  # Today's date (without time)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    return render(request,"adminpanelapp/login.html")

def Logindata(request):
     if request.POST.get('submit')=="Submit":
        luser=request.POST.get('username')
        lpass=request.POST.get('password')

        if luser and lpass:
            user=SuperAdmin.objects.filter(username=luser,password=lpass).first()
            if user:
                userid=request.session['member']=user.id
                return redirect("home")
            else:
               return redirect("login")
            
def Register(request):
    if request.POST.get('submit')=="Submit":
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if name and email and username and password:
            SuperAdmin.objects.create(name=name,email=email,username=username,password=password)
            return redirect("login")
        else:
            return render(request,"adminpanelapp/register.html")
    return render(request,"adminpanelapp/register.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(request):
    return render(request, "adminpanelapp/index.html")


def add_category(request):
     if request.POST.get('submit')=="Submit": 
        id=request.POST.get('id')
        category=request.POST.get('category')
        if (id):
            Category.objects.filter(id=id).update(category_name=category)
            return redirect("category")
        else:
            Category.objects.create(category_name=category)
            return redirect("category")
     name=request.GET.get('search','')
     if name:
        categorydata=Category.objects.filter(category_name__icontains=name)
     else:
        categorydata=Category.objects.all()
     return render(request,"adminpanelapp/category.html",{"categorydata":categorydata,"name":name})


def Editdata(request):
    editid=request.GET.get('editid')
    editdata=Category.objects.filter(id=editid).first()
    categorydata=Category.objects.all()
    return render(request,"adminpanelapp/category.html",{'alledit':editdata,"categorydata":categorydata} )

def deletedata(request):
    delid=request.GET.get('delid')
    Category.objects.get(id=delid).delete()
    return redirect("category")


def add_product(request):
    if request.POST.get('submit')=="Submit":
        id=request.POST.get('id')
        Category_id=request.POST.get('Category_id')
        Name=request.POST.get('Name')
        Price=request.POST.get('Price')
        photo=request.FILES['photo']
        Discription=request.POST.get('Discription')
        available_qty=request.POST.get('available_qty')
        
        if id:
            category=Category.objects.get(id=Category_id)
            select_product = Products.objects.get(id=id)
           

            select_product.category_id = category
            select_product.product_name = Name
            select_product.product_price = Price
            select_product.product_image = photo
            select_product.product_discription = Discription
            select_product.available_qty = available_qty

            select_product.save()
            return redirect("product")
        else:
            category=Category.objects.get(id=Category_id)
            Products.objects.create(category_id=category,product_name=Name,product_price=Price,product_image=photo,product_discription=Discription,available_qty=available_qty)
            return redirect("product")
    categorydata=Category.objects.all()
    productdata=Products.objects.all()
    return render(request,"adminpanelapp/product.html",{"productdata":productdata,"categorydata":categorydata})

def Productedit(request):
    proeditid=request.GET.get("proeditid")
    proeditdata=Products.objects.filter(id=proeditid).first()
    productdata=Products.objects.all()
    categorydata=Category.objects.all()
    
    return render(request,"adminpanelapp/product.html",{"proeditdata":proeditdata,"productdata":productdata,"categorydata":categorydata})

def Productdelete(request):
    prodelid=request.GET.get('prodelid')
    Products.objects.get(id=prodelid).delete()
    return redirect("product")

def Orderdata(request):
    if request.POST.get('submit')=="Submit":
        id=request.POST.get('id')
        Name=request.POST.get('name')
        Add=request.POST.get('add')
        Contact=request.POST.get('contact')
        total_amout=request.POST.get('tamount')
        Status=request.POST.get('status')
        if id:
            order_product=Order.objects.get(id=id)
            order_product.customer_fname=Name
            order_product.customer_address=Add
            order_product.email=Contact
            order_product.total_amount=total_amout
            order_product.status=Status

            order_product.save()
            return redirect("order")

    order_list = Order.objects.all()
    return render(request,"adminpanelapp/order.html",{"order_list":order_list})

def Editorder(request):
    edit_order=request.GET.get("editorder")
    orderedit=Order.objects.filter(id=edit_order).first()
    order_list=Order.objects.all()
    return render(request,"adminpanelapp/order.html",{"orderedit":orderedit,"order_list":order_list})




        
