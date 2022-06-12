from .views import HomeView, ArticleDetailView, AddPostView
from django.urls import path, include

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('addPost/', AddPostView.as_view(), name='addPost'),
]
