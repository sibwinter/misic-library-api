from backend.models import Album, Author, Song
from .serializers import AlbumSerializer, AuthorSerializer, SongSerializer

from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint shows all songs in albums.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows all authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that shows all authors.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [permissions.IsAuthenticated]
