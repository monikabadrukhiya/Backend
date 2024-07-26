from django.shortcuts import render,HttpResponse

def Home(request):
    return HttpResponse("<h1> this is my home page<h1>")

def About(request):
    return HttpResponse(" <h2 align=center color=green> this is my about page</h2>")

def Blog(request):
    return HttpResponse(" this blog page")

def Contact(request):
    return HttpResponse("your contact please")

def Design(request):
     return render(request,"home.html")

def Result(request):
    
    student_list = [
        {'Name':'Monika','Biology':910,'Physics':80,'Chemistry':96,'English':78},
        {'Name':'Khushal','Biology':70,'Physics':67,'Chemistry':90,'English':74},
        {'Name':'Panvi','Biology':71,'Physics':72,'Chemistry':65,'English':69},
        {'Name':'Mayur','Biology':62,'Physics':75,'Chemistry':80,'English':78},
    ]
   

    for std in student_list:
        total=[std['Biology'],std['Physics'],std['Chemistry'],std['English']]
        std["Total"]=sum(total)
        std["Minimum"]=min(total)
        std["Maximum"]=max(total)
        std["Persentage"]=round((std["Total"]/4),2)

        if std["Persentage"]>=90:
            std["Grade"]='A'
        elif std["Persentage"]>=80:
            std["Grade"]='B'
        elif std["Persentage"]>=70:
            std["Grade"]='C'
        elif std["Persentage"]>=60:
            std["Grade"]='D'
        else:
            std["Grade"]='F'       
    return render(request,"result.html",{'student_list':student_list})

