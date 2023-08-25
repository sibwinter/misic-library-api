from django.contrib import admin

from backend.models import Album, Author, Song, SongInAlbum

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

@admin.register(SongInAlbum)
class SongInAlbumAdmin(admin.ModelAdmin):
    list_display = ('pk','album')