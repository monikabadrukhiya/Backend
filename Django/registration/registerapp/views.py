from django.shortcuts import render,redirect,HttpResponse
from registerapp.models import Login
# Create your views here.
def Home(request):
    Data=Login.objects.all()
    return render(request,"form.html",{'data':Data})

def Getdata(request):
    if request.POST.get('submit')=='Submit':
        id=request.POST.get('id')
        name=request.POST.get('name')
        number=request.POST.get('number')
        gender=request.POST.get('gender')
        hobby=request.POST.getlist('hobby')
        city=request.POST.get('city')
        print("id==========",id)
        print(name)
        print(number)
        print(gender)
        print(hobby)
        print(city)
        hobby_list=','.join(hobby)
        print(hobby_list)
        if id != "":
            Login.objects.filter(id=id).update(Name=name,ContactNo=number,Gender=gender,Hobby=hobby_list,City=city)
        else:
            Login.objects.create(Name=name,ContactNo=number,Gender=gender,Hobby=hobby_list,City=city)
        return redirect("/")
    
def Delete(request):
    delid=request.GET.get('deleteid')
    if(delid and int(delid)>0):
        Login.objects.get(id=int(delid)).delete()
    return redirect("/")

def Edituser(request):
    edituser=request.GET.get('editid')
    alldata= Login.objects.filter(id=edituser).first()
    print("alldata========================",alldata)
    return render(request,"form.html",{'alldata':alldata})
