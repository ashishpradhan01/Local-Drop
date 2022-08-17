from django.contrib import admin

from .models import Movie, Music, Video

# Register your models here.

admin.site.register(Video)
admin.site.register(Music)
admin.site.register(Movie)