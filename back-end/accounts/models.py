from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from movies.models import Movie

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    collections = models.ManyToManyField(Movie, symmetrical=False, related_name='collected_movie')
    username = models.EmailField(unique=True)
    status = models.TextField()
    nickname = models.CharField(max_length=150, unique=True)
    profile_pic = ProcessedImageField(
    		blank = True,
        	upload_to = 'profile/images',
        	processors = [ResizeToFill(300, 300)],
        	format = 'JPEG',
        	options = {'quality':90},
    		)