from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from innovation.models import Innovation, Media, Category

class InnovationSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    #uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Innovation
        fields = '__all__'
        
      

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         