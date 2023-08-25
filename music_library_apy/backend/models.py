from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Имя исполнителя'
    )

    def __str__(self):
        return f"Автор: {self.name}"
    

class Album(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название альбома'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Альбом',
    )
    year_of_release = models.PositiveSmallIntegerField(
    
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return f"Альбом: {self.name}"


class Song(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название песни',
    )
    album = models.ManyToManyField(
        Album,
        through='SongsInAlbums',  
    )
    def __str__(self):
        return f"название песни: {self.name}"
    




class SongsInAlbums(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Альбом',
        related_name='songs'

    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name='Песня',
        related_name='albums'
    )
    number_in_album = models.PositiveSmallIntegerField(
        verbose_name='Номер песни в альбоме',
    )

    def __str__(self):
        return f"в альбоме {self.album} {self.number_in_album}: {self.song}"
    
    @property
    def song_name(self):
        return self.song
    