from django.shortcuts import render,redirect,HttpResponse
from studentpanelapp .models import Signdata,Admission,Inquiry
from django.views.decorators.cache import cache_control
from datetime import date

today = date.today()  # Today's date (without time)
print("Today========", today)

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    return render(request,"login.html")

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Home(request):
    # Query for inquiries with expected and visited dates matching today
    today_calls = Inquiry.objects.filter(expectedDate__date=today).count()
    inquiry_count = Inquiry.objects.filter(visitedDate__date=today).count()

    print("Today calls====", today_calls)
    print("Inquiry count====", inquiry_count)

    # Initialize overdue calls counter
    total_due_call = 0

    # Iterate through inquiries to count overdue tasks
    inquiries = Inquiry.objects.all()
    for inquiry in inquiries:
        expected_date = inquiry.expectedDate.date()  # Convert datetime to date
        print("Expected Date========", expected_date)

        # Check if the expected date is overdue
        if expected_date <today:
            total_due_call += 1

    # Render the data to the template
    return render(request, "index.html",  { 'todaycalls': today_calls,'inquirycount': inquiry_count,'totalduecall': total_due_call }
    )



def Todaycall(request):
     print("Today========",today)
     showtodaycalldata=Inquiry.objects.filter(expectedDate=today)
     return render(request,"showtodaycall.html",{'showtodaycalldata':showtodaycalldata})


def Countinquiry(request):
     print("Today========",today)
     countinquirydata=Inquiry.objects.filter(visitedDate=today)
     return render(request,"showcountinquiry.html",{'countinquirydata':countinquirydata})

def Duecalls(request):
    inquiries = Inquiry.objects.all()
    for inquiry in inquiries:
        expected_date = inquiry.expectedDate.date()  # Convert datetime to date
    dueinquirydata=Inquiry.objects.filter(expectedDate__lt=today)
    return render(request,"showduecall.html",{'dueinquirydata':dueinquirydata})

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
        expectedate=request.GET.get('expectedate')
        visiteddate=request.GET.get('visiteddate')
        status=request.GET.get('status')
        print("id=====",id)
        print("name======",name)
        print("name======",num)
        print("name======",pnum)
        print("name======",study)
        print("name======",ref)
        print("date========",expectedate)
        print("name======",inquiry)
       
        if (id):
            Inquiry.objects.filter(id=id).update(Name=name,Number=num,Pnumber=pnum,Study=study,Reference=ref,Inquiry=inquiry,expectedDate=expectedate,visitedDate=visiteddate,Status=status)
            return redirect("/viewdata")
        else:
            Inquiry.objects.create(Name=name,Number=num,Pnumber=pnum,Study=study,Reference=ref,Inquiry=inquiry,expectedDate=expectedate,visitedDate=visiteddate,Status=status)
            return redirect("/home")
                    
def Editdata(request):
    editid=request.GET.get('editid')
    print("editid======",editid)
    editdata=Inquiry.objects.filter(id=editid).first()
    return render(request,"addforms-layouts.html",{'alledit':editdata} )




