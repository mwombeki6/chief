from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from innovation.models import Innovation, Media, Category

class InnovationSerializer(serializers.ModelSerializer):
    
    #innovation_count = serializers.SerializerMethodField()

    class Meta:
        model = Innovation
        fields = ( 'category', 'innovation_name', 'slug', 'abstract', 'innovation_file', 'uploaded_at', 'uploaded_by', 'status')
  

   # def get_uploaded_by(self, obj):
    #    return obj.uploaded_by.all()  

    #def get_innovation_count(self, obj):
     #   return len(obj.innovation_file.all()) 
        

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         