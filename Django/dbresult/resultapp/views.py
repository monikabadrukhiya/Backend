from django.shortcuts import render,redirect
from resultapp.models import Login

def Home(request):
    data=Login.objects.all()
    return render(request,"home.html",{"data":data})

def Adddata(request):
    id=request.GET.get('id')
    print("iiiiiiiddddd",id)
    name=request.GET.get('name')
    maths=request.GET.get('maths')
    sci=request.GET.get('sci')
    phy=request.GET.get('phy')

    print("name=========",name)
    total=int(maths)+int(sci)+int(phy)
    per=total / 3
    
    if(name and int(maths) and int(sci) and int(phy)):
        Login.objects.filter(id=id).update(name=name,maths=int(maths),sci=int(sci),phy=int(phy),total=total,per=per)
        return redirect("/")
    else:
        Login.objects.create(name=name,maths=int(maths),sci=int(sci),phy=int(phy),total=total,per=per)
        return redirect("/")
    
def Delete(request):
    id=request.GET.get("id")
    if(id and int(id)>0):
        Login.objects.get(id=int(id)).delete()
    return redirect("/")

def Editdata(request):
    editid=request.GET.get("editid")
    all=Login.objects.filter(id=editid).first()
    return render(request,"home.html",{"all":all})
