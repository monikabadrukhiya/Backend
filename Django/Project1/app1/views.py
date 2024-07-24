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
    a={
        "Name":"monika",
        "marks":[98,56,78],
    }
    return render(request,"result.html",{"a":a})

