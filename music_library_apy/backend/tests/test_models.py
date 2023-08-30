from backend.models import Author, Album
from backend.serializers import AuthorSerializer
from backend.serializers import AlbumSerializer

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_authors(client):
    url = reverse('authors-list')
    response = client.get(url)
    authors = Author.objects.all()
    expected_data = AuthorSerializer(authors, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_get_albums(client):
    url = reverse('albums-list')
    response = client.get(url)
    albums = Album.objects.all()
    expected_data = AlbumSerializer(albums, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data
