# Generated by Django 4.2.4 on 2023-08-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_album_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(through='backend.SongsInAlbums', to='backend.album'),
        ),
    ]