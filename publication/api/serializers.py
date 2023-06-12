from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from publication.models import Publication, Category

class PublicationSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SerializerMethodField()
    publication_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Publication
        fields = ('category', 'publication_name', 'slug', 'abstract', 'published_file', 'pages', 'publisher', 'published_at', 'uploaded_by', 'authors', 'publication_count')

    def get_uploaded_by(self, obj):
        return obj.uploaded_by.username   

    def get_publication_count(self, obj):
        return len(obj.published_file.all())     
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         