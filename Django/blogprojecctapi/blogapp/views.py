from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapp.models import Blog,Comment
from blogapp.blogserializer import Blogserializer,Commentserializer


@api_view(['GET'])
def Blogget(request):
    data=Blog.objects.all()
    Blogdata=Blogserializer(data,many=True)
    return Response({"data":Blogdata.data})

@api_view(['POST'])
def Blogcreate(request):
    print(request.data)
    serializer=Blogserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data})
    print(serializer.errors)
    return Response({'data':[],"error":"Enter valid field"})

@api_view(['GET'])
def Blogfilter(request,bfilterid):
    print(bfilterid)
    filterdata=Blog.objects.filter(id=bfilterid)

    serializer=Blogserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['GET'])
def Userblogfilter(request,userblogfilter):
    print(userblogfilter)
    filterdata=Blog.objects.filter(userName=userblogfilter)

    serializer=Blogserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['GET'])
def categoryblogfilter(request,categoryblogfilter):
    print(categoryblogfilter)
    filterdata=Blog.objects.filter(categoryName=categoryblogfilter)

    serializer=Blogserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['DELETE'])
def Blogdelete(request,bdeleteid):
    data=Blog.objects.filter(id=bdeleteid)
    data.delete()
    return Response({"data":[],"error":"Delete Blog"})

@api_view(['PUT'])
def Blogupdate(request,bupdateid):
    username=request.data['userName']
    categoryname=request.data['categoryName']
    blogimage=request.data['blogimage']
    blogtitle=request.data['blogtitle']
    description=request.data['description']
    

    filterdata=Blog.objects.filter(id=bupdateid).update(userName=username,categoryName=categoryname,
                                    blogimage=blogimage,blogtitle=blogtitle,description=description)
    return Response({'data':"Update user"})

@api_view(['POST'])
def Commentcreate(request):
    print(request.data)
    serializer=Commentserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data})
    print(serializer.errors)
    return Response({'data':[],"error":"Enter valid field"})

@api_view(['GET'])
def Commentfilter(request,filterid):
    print(filterid)
    filterdata=Comment.objects.filter(id=filterid)

    serializer=Commentserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['GET'])
def Commentblogfilter(request,commentblogfilter):
    print(commentblogfilter)
    filterdata=Comment.objects.filter(userid=commentblogfilter)

    serializer=Commentserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['GET'])
def Commentuserfilter(request,commentuserfilter):
    print(commentuserfilter)
    filterdata=Comment.objects.filter(userid=commentuserfilter)

    serializer=Commentserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['DELETE'])
def Commentdelete(request,deleteid):
    data=Comment.objects.filter(id=deleteid)
    data.delete()
    return Response({"data":"Delete Blog"})

@api_view(['PUT'])
def Commentupdate(request,updateid):
    userid=request.data['userid']
    blogid=request.data['blogid']
    comment=request.data['comment']
    date=request.data['date']
    
    Comment.objects.filter(id=updateid).update(userid=userid,blogid=blogid,comment=comment,
                                                          date=date)
    return Response({'data':"Update user"})



