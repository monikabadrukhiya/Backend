from django.shortcuts import render,HttpResponse

def Home(request):
    return HttpResponse("hello")

def Result(request):
    Name=input("Enter Name=")
    Bio=int(input("Enter Marks="))
    Chem=int(input("Enter Marks="))
    Phy=int(input("Enter Marks="))
    Eng=int(input("Enter Marks="))

    student_list=[{'Name':Name,'Biology':Bio,'Chemistry':Chem,'Physics':Phy,'English':Eng}]

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
