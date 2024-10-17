from rest_framework import serializers
from .models import Blog
from.models import Comment
from userapp.userserializer import UserSerializer
from catagoryapp.categoryserializer import Categoryserializer

class Blogserializer(serializers.ModelSerializer):
    # userName=UserSerializer()
    # categoryName=Categoryserializer()
    # userName=serializers.StringRelatedField()
    # categoryName=serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['Firstname']

class Commentserializer(serializers.ModelSerializer):
    # userid=UserSerializer()
    # blogid=Blogserializer()
    # userid=serializers.StringRelatedField()
    # blogid=serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['Firstname']
    
