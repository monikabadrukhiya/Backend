from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from authuser.models import authusermodel
from authuser.serializer import authusermodelSerializer
from django.contrib.auth.hashers import make_password,check_password



@api_view(['POST'])                            
def Signup(request):
    name=request.data["Name"]
    username=request.data["Username"]
    email=request.data["Email"]
    password=request.data["Password"]

    print("getdata===========",name,username,email,password)
    if name and username and password and email:
        ckeckemaildata=authusermodel.objects.filter(Email=email)
        if ckeckemaildata:
            return Response({'data':[],"error":"Email Already Exist"})
        else:
            request.data['Password']=make_password(request.data["Password"])
            serializer=authusermodelSerializer(data=request.data)
            print("name=====",request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
            else:
                # print(serializer.errors)
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
                # return Response({'data':[],"error":"not valid field"},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'data':[],"error":"Please Enter valid field"},status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])                            
def Login(request):
    email=request.data["Email"]
    password=request.data["Password"]


    print(email,password)
    if email and password:
        checkemaildata=authusermodel.objects.filter(Email=email)
        if checkemaildata:
            checkpass=check_password(password,checkemaildata[0].Password)
            if checkpass:
                serializer=authusermodelSerializer(checkemaildata[0])
                return Response({'data':serializer.data,"message":"login successful"},status=status.HTTP_200_OK)
            else:
                return Response({'data':[],"error":"please Enter valid password"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'data':[],"error":"user is not valid" },status=status.HTTP_404_NOT_FOUND)
    else:
        return Response ({'data':[],"error":"user is not Field" },status=status.HTTP_404_NOT_FOUND)
            
    