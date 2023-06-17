from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from research.models import Research, Media, Category

class ResearchSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Research
        fields = ('category', 'research_name', 'slug', 'abstract', 'status')

  
        
      

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         