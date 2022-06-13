from .views import HomeView, ArticleDetailView, AddPostView, DeletePostView
from django.urls import path, include

from django.conf.urls import handler404

handler404 = 'zmienpiec.views.handler404'


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('addPost/', AddPostView.as_view(), name='addPost'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='deletePost'),
]
