from rest_framework import serializers
from .models import authusermodel

class authusermodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = authusermodel
        fields = '__all__'
        # fields = ['Firstname']