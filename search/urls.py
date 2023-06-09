from django.urls import path
from .views import SearchUsers, search_view

urlpatterns = [
    path('user/<str:query>', search_view),
    path('user/', SearchUsers.as_view())
]