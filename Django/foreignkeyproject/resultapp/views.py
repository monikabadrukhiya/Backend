from rest_framework.decorators import api_view
from rest_framework.response import Response
from resultapp.models import Result
from resultapp.resultserialiser import ResultSerializer




@api_view(['GET'])
def Resultget(request):
    data=Result.objects.all()
    Resultdata=ResultSerializer(data,many=True)
    return Response({'data':Resultdata.data})

@api_view(['POST'])
def Resultcreate(request):
    print(request.data)
    userserializer=ResultSerializer(data=request.data)

    if userserializer.is_valid():
        userserializer.save()
        return Response({'data':userserializer.data})
    return Response({'data':[],"error":"Enter Valid Fields"})

@api_view(['GET'])
def Resultfilter(request,rfilterid):
    print(rfilterid)
    data=Result.objects.filter(id=rfilterid)

    alldata=ResultSerializer(data,many=True)
    return Response({'data':alldata.data})

@api_view(['DELETE'])
def Resultdelete(request,rdeleteid):
    data=Result.objects.filter(id=rdeleteid)
    data.delete()
    return Response({'data':"Delete user"})

@api_view(['PUT'])
def Resultupdate(request,rupdateid):
    Username=request.data['userName']
    sci=request.data['science']
    maths=request.data['maths']
    phy=request.data['physics']
    
    Result.objects.filter(id=rupdateid).update(userName=Username,science=sci,maths=maths,physics=phy)
    return Response({'data':"Update user"})


