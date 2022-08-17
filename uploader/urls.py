from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('video/', video, name='video_list'),
    path('video/<int:pk>', delete_video, name='delete_video'),
    path('video/p/<int:pk>', play_video, name='play_video'),
    path('music/', music, name='music_list'),
    path('music/<int:pk>', delete_music, name='delete_music'),
    path('music/p/<int:pk>', play_music, name='play_music'),
    path('movie/', movie, name='movie_list'),
    path('movie/<int:pk>', delete_movie, name='delete_movie'),
    path('movie/p/<int:pk>', play_movie, name='play_movie'),
]