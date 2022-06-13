from cProfile import label
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'type': 'hidden', 'value': '', 'id': 'authorInput'}),
        }
        labels = {
            'title': 'Tytuł',
            'body': 'Treść:',
            'header_image': 'Obraz nagłówkowy',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body', 'post')

        widgets = {
            'author': forms.TextInput(attrs={'type': 'hidden', 'value': '', 'id': 'authorInput'}),
            'post': forms.TextInput(attrs={'type': 'hidden', 'value': '', 'id': 'postInput'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'body': '',
        }
