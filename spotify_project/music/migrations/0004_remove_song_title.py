# Generated by Django 4.2.13 on 2024-06-22 09:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0003_song_audio_file_song_cover_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="title",
        ),
    ]
