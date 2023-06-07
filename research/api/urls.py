from django.urls import path
from .views import uploadView, categoryView, mediaView, getCategories, getResearch, CategoryItemView, ResearchView

urlpatterns = [
    path("upload-research", uploadView),
    path("category-innovation", categoryView),
    path("media-innovation", mediaView),
    path("get-categories", getCategories),
    path('get-category/<slug:slug>/', CategoryItemView.as_view()),
    path("get-researches", getResearch),
    path("get-research/<slug:slug>", ResearchView.as_view())
]