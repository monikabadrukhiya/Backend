from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tokensapp.models import Tokenmodel
from tokensapp.serializer import TokenSerializer
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])                            
def Signup(request):
    username=request.data["username"]
    email=request.data["email"]
    password=request.data["password"]
    phone=request.data["phone"]


    print("getdata===========",phone,username,email,password)
    if phone and username and password and email:
        ckeckemaildata=Tokenmodel.objects.filter(email=email)
        if ckeckemaildata:
            return Response({'data':[],"error":"Email Already Exist"})
        else:
            request.data['password']=make_password(request.data["password"])
            serializer=TokenSerializer(data=request.data)
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
    email=request.data["email"]
    password=request.data["password"]   


    print(email,password)
    if email and password:
        checkemaildata=Tokenmodel.objects.filter(email=email)
        if checkemaildata:
            checkpass=check_password(password,checkemaildata[0].password)
            if checkpass:
                # serializer=TokenSerializer(checkemaildata[0])
                refresh = RefreshToken.for_user(checkemaildata[0])

                print("refresh====",refresh)
                return Response({"message":"login successful",'refresh': str(refresh),
                     'access': str(refresh.access_token),},status=status.HTTP_200_OK)
            else:
                return Response({'data':[],"error":"please Enter valid password"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'data':[],"error":"user is not valid" },status=status.HTTP_404_NOT_FOUND)
    else:
        return Response ({'data':[],"error":"user is not Field" },status=status.HTTP_404_NOT_FOUND)
            
    