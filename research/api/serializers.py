from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from research.models import Research, Media, Category

class ResearchSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    #uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Research
        fields = '__all__'
        
      

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         