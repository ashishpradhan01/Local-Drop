from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .form import MovieForm, MusicForm, VideoForm
from .models import Movie, Music, Video
import os

# Create your views here.

def home(request):
    return render(request, 'index.html')

def video(request):
    if request.POST:
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video successfully uploaded')
            return HttpResponseRedirect("/video")
        else:
            messages.error(request, "Something went wrong!")
    else:
        form = VideoForm()
    all_videos = Video.objects.all()
    return render(request, 'video/index.html', {'videos' : all_videos, 'form' : form})


def delete_video(request, pk) :
    video = Video.objects.get(pk = pk)
    video.delete()
    FILE_PATH = "."+video.video_file.url
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    return redirect('video_list')

def play_video(request, pk):
    video = Video.objects.get(pk = pk)
    return render(request, 'video/play.html', {'video' : video})

# -------------------------------------------------------------------------------------------------------------

def music(request):
    if request.POST:
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Music successfully uploaded')
            return HttpResponseRedirect("/music")
        else:
            messages.error(request, "Something went wrong!")
    else:
        form = MusicForm()
    all_music = Music.objects.all()
    return render(request, 'music/index.html', {'music' : all_music, 'form' : form})


def delete_music(request, pk) :
    music = Music.objects.get(pk = pk)
    music.delete()
    FILE_PATH = "."+music.music_file.url
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    return redirect('music_list')

def play_music(request, pk):
    music = Music.objects.get(pk = pk)
    return render(request, 'music/play.html', {'music' : music})

# -------------------------------------------------------------------------------------------------------------

def movie(request):
    if request.POST:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie successfully uploaded')
            return HttpResponseRedirect("/movie")
        else:
            messages.error(request, "Something went wrong!")
    else:
        form = MovieForm()
    all_movie = Movie.objects.all()
    return render(request, 'movie/index.html', {'movies' : all_movie, 'form' : form})


def delete_movie(request, pk) :
    movie = Movie.objects.get(pk = pk)
    movie.delete()
    FILE_PATH = "."+movie.movie_file.url
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    return redirect('movie_list')

def play_movie(request, pk):
    movie = Movie.objects.get(pk = pk)
    return render(request, 'movie/play.html', {'movie' : movie})