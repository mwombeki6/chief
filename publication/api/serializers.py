from custom.api.serializers import UserSerializer
from student.api.serializers import StudentSerializer
from rest_framework import serializers
from publication.models import Publication, Category

class PublicationSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    #uploaded_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Publication
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'         