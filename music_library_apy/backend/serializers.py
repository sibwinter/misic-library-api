from backend.models import Album, Author, Song, SongsInAlbums
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Author
        fields = ['name',]


class SongsInAlbumsSerializer(serializers.ModelSerializer):    
    song_name = serializers.ReadOnlyField(source='song.name')

    class Meta:
        model = SongsInAlbums
        fields = ['song_name','number_in_album']
        


class AlbumSerializer(serializers.ModelSerializer):    
    songs = SongsInAlbumsSerializer(many=True)

    class Meta:
        model = Album
        fields = ['pk','name', 'year_of_release', 'songs']
        

class SongsAlbumsSerializer(serializers.ModelSerializer):    
    album_name = serializers.ReadOnlyField(source='album.name')

    class Meta:
        model = SongsInAlbums
        fields = ['album_name','number_in_album']
        

class SongSerializer(serializers.ModelSerializer):   
    albums = SongsAlbumsSerializer(many=True)
    
    class Meta:
        model = Song
        fields = ['pk','albums']
        
