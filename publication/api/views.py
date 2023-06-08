from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (    
    exceptions as rest_exceptions,
    response,
    decorators as rest_decorators,
    permissions as rest_permissions,
)
from rest_framework import generics
from .. import models
from ..models import Publication, Category
from .serializers import PublicationSerializer, CategorySerializer

    
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([rest_permissions.AllowAny])    
def categoryView(request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    category = serializer.save()
    
    if category is not None:
        return response.Response({'category': serializer.data})
    
    return rest_exceptions.status
   
  
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([rest_permissions.AllowAny])
def uploadView(request):
    serializer = PublicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    publication = serializer.save()
    
    if publication is not None:
        return response.Response({
            'research': serializer.data, 
            'message': 'Publication uploaded successfully'
        })   
        
    return rest_exceptions.status    

        
@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.AllowAny]) 
def getCategories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

class CategoryItemView(generics.ListAPIView):
    serializer_class = PublicationSerializer
    
    def get_queryset(self):
        return models.Publication.objects.filter(
            category__in = Category.objects.get(slug=self.kwargs['slug']).get_descendants(include_self = True)
        )

@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.AllowAny]) 
def getPublication(request):
    publication = Publication.objects.all()
    serializer = PublicationSerializer(publication, many=True)
    return Response(serializer.data)

class PublicationView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
        