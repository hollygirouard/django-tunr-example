# Generated by Django 4.0.2 on 2022-02-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0003_song_album_song_preview_url_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(default='no album title', max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(default='no song title', max_length=100),
        ),
    ]
