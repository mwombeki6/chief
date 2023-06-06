from django.shortcuts import render
from rest_framework import viewsets

from notification.models import Notification
from .serializers import NotificationSerializer

class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer