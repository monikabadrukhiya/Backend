from rest_framework.decorators import api_view
from rest_framework.response import Response
from educationapp.models import Education
from educationapp.educationserializer import EducationSerializer

@api_view(['GET'])
def Eduget(request):
    data=Education.objects.all()

    edudata=EducationSerializer(data,many=True)
    return Response({'data':edudata.data})

@api_view(['POST'])
def Educreate(request):
    print(request.data)
    userserializer=EducationSerializer(data=request.data)

    if userserializer.is_valid():
        userserializer.save()
        return Response({'data':userserializer.data})
    return Response({'data':[],"error":"Enter Valid Fields"})

@api_view(['GET'])
def Edufilter(request,efilterid):
    print('ef==',efilterid)

    data=Education.objects.filter(id=efilterid)

    alldata=EducationSerializer(data, many=True)
    return Response({'data':alldata.data})


@api_view(['DELETE'])
def Edudelete(request,edeleteid):
    print('ef==',edeleteid)
    data=Education.objects.filter(id=edeleteid)
    data.delete()
    return Response({'data':"Delete users"})


@api_view(['PUT'])
def Eduupdate(request,eupdateid):
    print('eu======',eupdateid)
    username=request.data['userName']
    education=request.data['education']
    skill=request.data['skills']

    Education.objects.filter(id=eupdateid).update(userName=username,education=education,skills=skill)
    return Response({'data':"Update users"})



