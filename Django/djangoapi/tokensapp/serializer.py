from rest_framework import serializers
from .models import Tokenmodel

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokenmodel
        fields = '__all__'
        # fields = ['Firstname']