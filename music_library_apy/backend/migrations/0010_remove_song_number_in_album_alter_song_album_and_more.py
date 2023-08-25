# Generated by Django 4.2.4 on 2023-08-25 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_album_songs_song_album_song_number_in_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='number_in_album',
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='backend.album', verbose_name='Альбом'),
        ),
        migrations.CreateModel(
            name='SongsInAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_in_album', models.PositiveSmallIntegerField(verbose_name='Номер песни в альбоме')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.album', verbose_name='Альбом')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='backend.song', verbose_name='Альбом')),
            ],
        ),
    ]