# spotify_project/urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', views.song_list, name='song_list'),
    path('', views.akhil, name='akhil'),
    path('play/', views.play, name='play'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
