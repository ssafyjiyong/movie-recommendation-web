from django.db import models
from django.conf import settings

from movies.models import Movie
# Create your models here.

class Article(models.Model):
    categories = [
    ('talk', 'talk'),
    ('toon', 'toon'),
    ('ticket', 'ticket'),

    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='articles'
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )
    category = models.CharField(max_length=10, choices=categories)
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Image(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     article_img = models.ImageField(null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_comments'
    )
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class Recomment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recomments'
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
