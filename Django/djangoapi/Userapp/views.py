from rest_framework.decorators import api_view
from rest_framework.response import Response
from Userapp.models import User
from Userapp.serializers import UserSerializer

@api_view(['GET'])                            # Data  GET 
def Getuser(request):
    data=User.objects.all()                    # Get data
    alldata=UserSerializer(data,many=True)               # convert into json

    return Response({"data":alldata.data})


@api_view(['POST'])                            # Data  Add 
def Creatuser(request):
    print(request.data)
    serializer=UserSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()
        return Response({"data":serializer.data})
    return Response({"data":[],"error":"Please Enter Valid Field"})

@api_view(['GET'])                            # Data  Add 
def Filteruser(request,filterid):
    print(filterid)
    data=User.objects.filter(id=filterid)
    alldata=UserSerializer(data,many=True) 

    return Response({"data":alldata.data})

@api_view(['DELETE'])                            # Data  Add 
def Deleteuser(request,delid):
    print(delid)
    data=User.objects.filter(id=delid)
    data.delete()

    return Response({"Message":"Delete User"})


@api_view(['PUT'])                            # Data  Add 
def Updateuser(request,updateid):
    print(updateid)
    fname=request.data['Firstname']
    lname=request.data['Lastname']
    email=request.data['Email']
    password=request.data['Password']
    num=request.data['Number']

    User.objects.filter(id=updateid).update(Firstname=fname,Lastname=lname,Email=email,Password=password,Number=num)
    

    return Response({"Message":"Update User"})




