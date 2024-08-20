from django.shortcuts import render,redirect,HttpResponse
from cardapp.models import Form

def Home(request):
    data=Form.objects.all()
    return render(request,"home.html",{'data':data})

def Getdata(request):
        id=request.GET.get('id')
        header=request.GET.get('heading')
        disc=request.GET.get('description')
        readmore=request.GET.get('readmore')
        comment=request.GET.get('footer')
    
        if(id):
            Form.objects.filter(id=id).update(Header=header,Disctiption=disc,Readmore=readmore,footer=comment)
        else:
           Form.objects.create(Header=header,Disctiption=disc,Readmore=readmore,footer=comment)
        return redirect("/")
    
def Delete(request):
    delid=request.GET.get('deleteid')
    if(id and int(id)>=0):
     Form.objects.get(id=delid).delete()
     return redirect("/")
    
def Editdata(request):
    edid=request.GET.get('editid')
    alldata=Form.objects.get(id=edid)
    return render(request,"home.html",{'alldata':alldata})

def viewdata(request):
        data=Form.objects.all()
        return render(request,"card.html",{'data':data})
   
   

