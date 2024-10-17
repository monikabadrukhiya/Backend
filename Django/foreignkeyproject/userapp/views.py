from rest_framework.decorators import api_view
from rest_framework.response import Response
from userapp.models import User
from userapp.userserializer import UserSerializer


@api_view(['GET'])
def Getuser(request):
    data=User.objects.all()
    alldata=UserSerializer(data,many=True)
    return Response({'data':alldata.data})

@api_view(['POST'])
def Creatuser(request):
    print(request.data)
    userserializer=UserSerializer(data=request.data)

    if userserializer.is_valid():
        userserializer.save()
        return Response({'data':userserializer.data})
    return Response({'data':[],"error":"Please Enter valid Field"})


@api_view(['GET'])
def Filteruser(request, filterid ):
    print("filterid=====",filterid)
    data=User.objects.filter(id=filterid)

    alldata=UserSerializer(data,many=True)
    return Response({'data':alldata.data})

@api_view(['DELETE'])
def Deleteuser(request,deleteid):
    data=User.objects.filter(id=deleteid)
    data.delete()
    return Response({'data':"Delete User"})

@api_view(['PUT'])
def Updateuser(request, updateid):
    print("updateid=========",updateid)
    Username=request.data['userName']
    Email=request.data['email']
    pwd=request.data['password']
    User.objects.filter(id=updateid).update(userName=Username,email=Email,password=pwd)

    return Response({'data':"Update User"})


