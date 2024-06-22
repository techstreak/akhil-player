from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'audio_file', 'cover_image')
    fields = ('file_name', 'audio_file', 'cover_image')

admin.site.register(Song, SongAdmin)
