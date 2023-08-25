from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Имя исполнителя'
    )

    def __str__(self):
        return f"Автор: {self.name}"
    
class Song(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название песни',
    )

    def __str__(self):
        return f"название песни: {self.name}"
    

class Album(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название альбома'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='Альбом',
    )
    year_of_release = models.PositiveSmallIntegerField(
    
        blank=True, 
        null=True
    )
    songs = models.ManyToManyField(
        Song,
        through='SongInAlbum',
        related_name='album',
    )

    def __str__(self):
        return f"Альбом: {self.name}"


class SongInAlbum(models.Model):
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name='Песня',
        related_name='songs_in_album'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Альбом'
    )
    number_in_album = models.PositiveSmallIntegerField(
        verbose_name='Номер песни в альбоме'
    )

    def __str__(self):
        return f'Пеня {self.song} в альбоме {self.album} под номером {self.number_in_album}'