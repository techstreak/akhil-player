# music/models.py

from django.db import models

class Song(models.Model):
    file_name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)  # FileField for audio files
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)  # ImageField for cover images

    class Meta:
        db_table = 'songs'

    def __str__(self):
        return self.title
