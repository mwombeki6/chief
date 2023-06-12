from django.urls import path
from .views import uploadView, categoryView, mediaView, getCategories, getInnovation, CategoryItemView, InnovationView, InnovationUpdate, InnovationDelete

urlpatterns = [
    path("upload-innovation", uploadView),
    path("update-innovation/<int:pk>", InnovationUpdate.as_view()),
    path("delete-innovation/<int:pk>", InnovationDelete.as_view()),
    path("category-innovation", categoryView),
    path("media-innovation", mediaView),
    path("get-categories", getCategories),
    path('get-category/<slug:slug>/', CategoryItemView.as_view()),
    path("get-innovations", getInnovation),
    path("get-innovation/<slug:slug>", InnovationView.as_view())
]