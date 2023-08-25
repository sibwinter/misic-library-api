from backend.models import Album, Author, Song, SongInAlbum
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Author
        fields = ['name',]


class SongInAlbumSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Song
        fields = ['song',]


class AlbumSerializer(serializers.ModelSerializer):    


    class Meta:
        model = Album
        fields = ['name', 'year_of_release', 'songs']
        
