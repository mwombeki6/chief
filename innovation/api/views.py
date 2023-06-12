from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (    
    exceptions as rest_exceptions,
    response,
    decorators as rest_decorators,
    permissions as rest_permissions,
)
from rest_framework import generics
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.contrib.auth.decorators import login_required
from .. import models
from ..models import Innovation, Category, Media
from .serializers import InnovationSerializer, CategorySerializer, MediaSerializer
from notification.models import Notification
from custom.models import User

    
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
    serializer = InnovationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    innovation = serializer.save()
    
    if innovation is not None:
        return response.Response({
            'innovation': serializer.data, 
            'message': 'Innovation uploaded successfully'
        })   
    
    users = User.objects.exclude(id=request.user.id)
    message = f"{request.user.username} uploaded a file"
    notifications = []
    for user in users:
        notification = Notification(user=user, message=message)
        notifications.append(notification)
    Notification.objects.bulk_create(notifications)   

        
    return rest_exceptions.status

class InnovationUpdate(generics.UpdateAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer

class InnovationDelete(generics.DestroyAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer    

@rest_decorators.api_view(['PUT', 'PATCH'])
@rest_decorators.permission_classes([rest_permissions.AllowAny])

@rest_decorators.api_view(['DELETE'])
@rest_decorators.permission_classes([rest_permissions.AllowAny])    

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
    serializer_class = InnovationSerializer
    
    def get_queryset(self):
        return models.Innovation.objects.filter(
            category__in = Category.objects.get(slug=self.kwargs['slug']).get_descendants(include_self = True)
        )

@rest_decorators.api_view(['GET'])
@rest_decorators.permission_classes([rest_permissions.AllowAny]) 
def getInnovation(request):
    innovation = Innovation.objects.all()
    serializer = InnovationSerializer(innovation, many=True)
    return Response(serializer.data)

class InnovationView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
        