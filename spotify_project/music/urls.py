# music/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.song_list, name='song_list'),
    path('', views.akhil, name='akhil'),
    path('play/', views.play, name='play'),
]
