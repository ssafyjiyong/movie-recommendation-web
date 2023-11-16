from django.db import models
from django.conf import settings
import datetime


class Actor(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_path = models.TextField(null=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=50, null=False)
    profile_path = models.TextField(null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=20)
    overview = models.TextField()
    release_date = models.DateField(null=True, default=datetime.date.today)
    runtime = models.IntegerField(null=True)
    
    poster_path = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    
    budget = models.BigIntegerField()
    popularity = models.FloatField()
    tagline = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    words = models.TextField(null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_movies'
    )

    def __str__(self):
        return self.title
