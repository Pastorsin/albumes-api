from album.models import Album
from album.serializers import AlbumSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
