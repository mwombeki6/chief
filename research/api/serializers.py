from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from research.models import Research, Media, Category

class ResearchSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SerializerMethodField()
    research_count = serializers.SerializerMethodField()

    class Meta:
        model = Research
        fields = ('category', 'research_name', 'slug', 'abstract', 'research_file', 'uploaded_at', 'uploaded_by', 'research_duration', 'research_count')

    def get_uploaded_by(self, obj):
        return obj.uploaded_by.username   

    def get_research_count(self, obj):
        return len(obj.research_file.all())    
        
      

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         