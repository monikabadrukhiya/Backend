from django.shortcuts import render,redirect
from resultapp.models import Login

def Home(request):
    data=Login.objects.all()
    return render(request,"home.html",{"data":data})



def Adddata(request):
    name=request.POST.get('name')
    maths=request.POST.get('maths')
    sci=request.POST.get('sci')
    phy=request.POST.get('phy')

    print("name=========",name)
    
    if(name and maths and sci and phy):
        total=int(maths)+int(sci)+int(phy)
        per=total / 3

        Login.objects.create(name=name,maths=int(maths),sci=int(sci),phy=int(phy),total=total,per=per)
        return redirect("Home")
    
def Delete(request):
    id=request.GET.get("id")
    if(id and int(id)>0):
        Login.objects.get(id=int(id)).delete()
    return redirect("/")
