from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['Firstname']


    def validate(self,data):
            # if data['Firstname']=='test':
            #     raise serializers.ValidationError("Please Enter valid First Name")
            # return data

            if not data['Firstname'].isalpha():
                raise serializers.ValidationError("Please Enter valid First Name")
            if not data['Lastname'].isalpha():
                raise serializers.ValidationError("Please Enter valid Last Name")
            if not  data['Password'].isalnum():
                raise serializers.ValidationError("Please Enter valid Password")
            if len(data['Number']) !=10:
                raise serializers.ValidationError("Please Enter valid Number ")
            return data
