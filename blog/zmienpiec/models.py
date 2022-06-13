from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    header_image = models.ImageField(null=True, blank=True, upload_to=path_and_rename, default='images/no-image.png')
    class Meta:
        verbose_name_plural = 'Posty'
        verbose_name = 'Post'

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("article", args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Komentarze'
        verbose_name = 'Komentarz'

    def __str__(self) -> str:
        return str(self.author)+' | '+self.post.title + ' | ' + self.body[slice(50)]
