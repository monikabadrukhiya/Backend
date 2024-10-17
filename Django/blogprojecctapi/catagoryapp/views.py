from rest_framework.decorators import api_view
from rest_framework.response import Response
from catagoryapp.models import Category
from catagoryapp.categoryserializer import Categoryserializer


@api_view(['GET'])
def Categoryget(request):
    data=Category.objects.all()
    Categorydata=Categoryserializer(data,many=True)
    return Response({"data":Categorydata.data})

@api_view(['POST'])
def Categorycreate(request):
    print(request.data)
    serializer=Categoryserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data})
    return Response({'data':[],"error":"Enter valid field"})

@api_view(['GET'])
def Categoryfilter(request,cfilterid):
    print(cfilterid)
    filterdata=Category.objects.filter(id=cfilterid)

    serializer=Categoryserializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['DELETE'])
def Categorydelete(request,cdeleteid):
    data=Category.objects.filter(id=cdeleteid)
    data.delete()
    return Response({"data":[],"error":"Delete Category"})

@api_view(['PUT'])
def Categoryupdate(request,cupdateid):
    categoryName=request.data['categoryName']
    categoryimg=request.data['categoryimg']
    

    filterdata=Category.objects.filter(id=cupdateid).update(categoryName=categoryName,categoryimg=categoryimg)
    return Response({'data':"Update user"})
