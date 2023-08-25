# Generated by Django 4.2.4 on 2023-08-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_remove_album_song_album_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.album', verbose_name='Альбом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='number_in_album',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Номер песни в альбоме'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SongInAlbum',
        ),
    ]
