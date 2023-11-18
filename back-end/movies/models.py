from django.db import models
from django.conf import settings


class Actor(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_path = models.TextField(null=True)


class Director(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_path = models.TextField(null=True)


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    director = models.ManyToManyField(Director, related_name='movies')
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=20, null=True)
    overview = models.TextField(null=True)
    release_date = models.TextField(null=True)
    runtime = models.IntegerField(null=True)
    poster_path = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    tagline = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    video = models.TextField(null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )
    normal_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='normal_movies'
    )
    hate_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='hate_movies'
    )


class Album(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.TextField(null=True)