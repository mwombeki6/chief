from django.urls import path
from .views import uploadView, categoryView, mediaView, getCategories, getInnovation, CategoryItemView, InnovationView

urlpatterns = [
    path("upload-innovation", uploadView),
    path("category-innovation", categoryView),
    path("media-innovation", mediaView),
    path("get-categories", getCategories),
    path('get-category/<slug:slug>/', CategoryItemView.as_view()),
    path("get-innovations", getInnovation),
    path("get-innovation/<slug:slug>", InnovationView.as_view())
]