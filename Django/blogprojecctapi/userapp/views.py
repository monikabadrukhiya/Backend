from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import User
from userapp.userserializer import UserSerializer


@api_view(['GET'])
def Userget(request):
    data=User.objects.all()
    userdata=UserSerializer(data,many=True)
    return Response({"data":userdata.data})

@api_view(['POST'])
def Usercreate(request):
    print(request.data)
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"data":serializer.data})
    return Response({'data':[],"error":"Enter valid field"})

@api_view(['GET'])
def Userfilter(request,ufilterid):
    print(ufilterid)
    filterdata=User.objects.filter(id=ufilterid)

    serializer=UserSerializer(filterdata,many=True)
    return Response({'data':serializer.data})

@api_view(['DELETE'])
def Userdelete(request,udeleteid):
    data=User.objects.filter(id=udeleteid)
    data.delete()
    return Response({"data":[],"error":"Delete user"})

@api_view(['PUT'])
def Userupdate(request,uupdateid):
    username=request.data['userName']
    email=request.data['email']
    password=request.data['password']

    filterdata=User.objects.filter(id=uupdateid).update(userName=username,email=email,password=password)
    return Response({'data':"Update user"})
