from django.shortcuts import render,redirect,HttpResponse
from studentpanelapp .models import Signdata,Admission,Inquiry
from django.views.decorators.cache import cache_control
import datetime as dt



# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    return render(request,"login.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(request):
    d=dt.datetime.now()
    Today=d.date()
    print("Today========",Today)
    inquirydata=Inquiry.objects.filter(Date=Today).count()
    print("datteee====",inquirydata)
    return render(request,"index.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addform(request):
    return render(request,"addforms-layouts.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Viewform(request):
        name=request.GET.get('search','')
        if name:
            viewsdata=Inquiry.objects.filter(Name__icontains=name)
        else:
            viewsdata=Inquiry.objects.all()
        return render(request,"viewform.html",{"viewsdata":viewsdata,'name':name})

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Addmissionform(request):
    return render(request,"admissionform.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Register(request):
    if request.POST.get('submit')=="Submit":
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("name=======",name)
        print("name=======",email)
        print("name=======",username)
        print("name=======",password)

        if name and email and username and password:
            Signdata.objects.create(Name=name,Email=email,Username=username,Password=password)
            return redirect("/")
        else:
            return render(request,"register.html")
    return render(request,"register.html")
    

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logindata(request):
     if request.POST.get('submit')=="Submit":
        luser=request.POST.get('username')
        lpass=request.POST.get('password')
        print("name=======",luser)
        print("name=======",lpass)

        if luser and lpass:
            user=Signdata.objects.filter(Username=luser,Password=lpass).first()
            print("user=======",user)
            if user:
                userid=request.session['member']=user.id
                print("userid=========",userid)
                return redirect("/home")
            else:
               return redirect("/")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)         
def Deletedata(request):
    try:
        del request.session['member']
        return redirect("/")
    except:
        return redirect("/home")
            
def admissiondata(request):
    if request.POST.get('submit')=="Submit": 
        name=request.POST.get('name')    
        num=request.POST.get('num')    
        pnum=request.POST.get('pnum')    
        study=request.POST.get('study')    
        cource=request.POST.get('cource')    
        fees=request.POST.get('fess')    
        duration=request.POST.get('duration')    
        jdate=request.POST.get('joindate')    
        ref=request.POST.get('reference')    
        photo=request.POST.get('photo') 
    
        if name and num and pnum and study and cource and fees and duration and jdate and ref and photo:
            Admission.objects.create(Name=name,Number=num,Pnumber=pnum,Study=study,Cource=cource,Fees=fees,
                                     Duration=duration,Joindate=jdate,Reference=ref,Photo=photo)
            return redirect("/home")

def totaladmission(request):
    name=request.GET.get('search','')
    if name:
        admisiondata=Admission.objects.filter(Name__icontains=name)
    else:
        admisiondata=Admission.objects.all()
    return render(request,"total-admission.html",{"adata":admisiondata,'name':name})

def Inquirydata(request):
    if request.GET.get('submit')=="Submit": 
        id=request.GET.get('id')    
        name=request.GET.get('name')    
        num=request.GET.get('num')    
        pnum=request.GET.get('pnum')    
        study=request.GET.get('study')       
        ref=request.GET.get('reference')    
        inquiry=request.GET.get('inquiry') 
        date=request.GET.get('date')
        status=request.GET.get('status')
        print("id=====",id)
        print("name======",name)
        print("name======",num)
        print("name======",pnum)
        print("name======",study)
        print("name======",ref)
        print("date========",date)
        print("name======",inquiry)

        if (id):
            Inquiry.objects.filter(id=id).update(Name=name,Number=num,Pnumber=pnum,Study=study,Reference=ref,Inquiry=inquiry,Date=date,Status=status)
            return redirect("/viewdata")
        else:
            Inquiry.objects.create(Name=name,Number=num,Pnumber=pnum,Study=study,Reference=ref,Inquiry=inquiry,Date=date,Status=status)
            inquirydata=Inquiry.objects.filter(Date=date).first()
            print("datteee====",inquirydata)
            return redirect("/home")
def Editdata(request):

    editid=request.GET.get('editid')
    print("editid======",editid)
    editdata=Inquiry.objects.filter(id=editid).first()
    return render(request,"addforms-layouts.html",{'alledit':editdata} )




