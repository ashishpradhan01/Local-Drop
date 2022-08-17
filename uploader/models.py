from datetime import datetime
from django.db import models

# Create your models here.

class Video(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos')

class Music(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    music_file = models.FileField(upload_to='music')

class Movie(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    movie_file = models.FileField(upload_to='movies')