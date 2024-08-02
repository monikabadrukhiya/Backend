from django.shortcuts import render,HttpResponse,redirect
from inputdata.models import login

def Home(request):

    # if request.POST.get('submit') == 'Submit':
    #     username=request.POST.get('username')
    #     password=request.POST.get('pswd')

    user_list=login.objects.all()
   
    return render(request,"home.html",{'user_list':user_list})

def Adddata(request):
      id=request.GET.get('id')
      username=request.POST.get('username')
      password=request.POST.get('pswd')
      print("username=========",username)
      print("password=============",password)

      if(id):
           login.objects.filter(id=id).update(username=username,password=password)
      else:
        login.objects.create(username=username,password=password)      
      return redirect("/")

def Delete(request):
     id=request.GET.get('deleteid')
     print("delete=======",id)
     if(id and int(id)>0):
        login.objects.get(id=int(id)).delete()
     return redirect("/")

def Edituser(request):
     editid=request.GET.get('editid')
     print("edi====================",id)
     editdata=login.objects.filter(id=editid)
     return render(request,"home.html",{"editdata":editdata})

    


