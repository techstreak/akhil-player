# music/views.py

from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})


def akhil(request):
    songs = Song.objects.all()
    return render(request, 'akhil.html', {'songs': songs})



def play(request):
    songs = Song.objects.all()
    return render(request, 'play.html', {'songs': songs})




