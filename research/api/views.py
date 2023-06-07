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
from ..models import Research, Category, Media
from .serializers import ResearchSerializer, CategorySerializer, MediaSerializer

    
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
    serializer = ResearchSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    research = serializer.save()
    
    if research is not None:
        return response.Response({
            'research': serializer.data, 
            'message': 'Research uploaded successfully'
        })   
        
    return rest_exceptions.status    

@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([rest_permissions.AllowAny])
def mediaView(request):
    serializer = MediaSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    media = serializer.save()
    
    if media is not None:
        return response.Response({
            "media": serializer.data
        })
        
@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.AllowAny]) 
def getCategories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

class CategoryItemView(generics.ListAPIView):
    serializer_class = ResearchSerializer
    
    def get_queryset(self):
        return models.Research.objects.filter(
            category__in = Category.objects.get(slug=self.kwargs['slug']).get_descendants(include_self = True)
        )

@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.AllowAny]) 
def getResearch(request):
    research = Research.objects.all()
    serializer = ResearchSerializer(research, many=True)
    return Response(serializer.data)

class ResearchView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
        