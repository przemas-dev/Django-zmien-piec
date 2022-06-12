from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import PostForm, CommentForm
from django.urls import reverse


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-create_date']


class ArticleDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'article.html'
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse('article', args=(str(self.object.id)))

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
