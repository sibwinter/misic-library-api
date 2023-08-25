from backend.models import Album, Song

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import AlbumSerializer



class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticated]
