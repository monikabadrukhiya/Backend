from django.shortcuts import render,HttpResponse
from inputdata.models import login

def Home(request):

    if request.POST.get('submit') == 'Submit':
        username=request.POST.get('username')
        password=request.POST.get('pswd')
        login.objects.create(username=username,password=password)

    user_list=login.objects.all()
    return render(request,"home.html",{'user_list':user_list})

def Delete(request):
    # id=request.GET.get('id')
    
    return render(request,"home.html")
