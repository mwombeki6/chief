from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from publication.models import Publication, Category

class PublicationSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Publication
        fields = ('category', 'publication_name', 'slug', 'abstract', 'published_file', 'pages', 'publisher', 'published_at', 'uploaded_by', 'authors', 'status')

      
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         