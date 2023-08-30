from django.contrib import admin

from backend.models import Album, Author, Song, SongsInAlbums


# Register your models here.

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SongsInAlbums)
class SongsInAlbumAdmin(admin.ModelAdmin):
    list_display = ('album',)
