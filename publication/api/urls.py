from django.urls import path
from .views import uploadView, categoryView, getCategories, getPublication, CategoryItemView, PublicationView

urlpatterns = [
    path("upload-publication", uploadView),
    path("category-publication", categoryView),
    path("get-categories", getCategories),
    path('get-category/<slug:slug>/', CategoryItemView.as_view()),
    path("get-publications", getPublication),
    path("get-publication/<slug:slug>", PublicationView.as_view())
]