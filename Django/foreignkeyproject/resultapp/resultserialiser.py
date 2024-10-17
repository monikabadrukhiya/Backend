from rest_framework import serializers
from .models import Result
from userapp.userserializer import UserSerializer



class ResultSerializer(serializers.ModelSerializer):
    userName=UserSerializer()
    class Meta:
        model = Result
        # fields = ['Firstname']

        fields = '__all__'
        # fields = ['Firstname']
