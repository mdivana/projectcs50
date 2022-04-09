from time import timezone
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField() 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)