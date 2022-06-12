from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def home(request):
    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-create_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'
