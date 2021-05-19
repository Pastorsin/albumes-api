from album.helpers import generate_zip
from album.models import Album
from album.renderers import ZipRenderer
from album.serializers import AlbumSerializer, ExportAlbumSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=True,
            methods=['get'],
            serializer_class=ExportAlbumSerializer,
            renderer_classes=(ZipRenderer, ))
    def download(self, request, pk=None):
        album = self.get_object()
        zip_content = generate_zip(album)

        response = Response(zip_content)
        response['Content-Disposition'] = 'attachment; filename="album.zip"'

        return response
