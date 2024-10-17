from rest_framework import serializers
from .models import Education

class EducationSerializer(serializers.ModelSerializer):
    userName=serializers.StringRelatedField()
    class Meta:
        model = Education
        fields = ['userName','skills']

        # fields = '__all__'
        # fields = ['Firstname']
