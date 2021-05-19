from album.helpers import generate_zip
from album.models import Album
from album.serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import viewsets, renderers
from rest_framework.decorators import action


class ZipRenderer(renderers.BaseRenderer):
    media_type = 'application/zip'
    file_format = 'zip'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=True, methods=['get'], renderer_classes=(ZipRenderer, ))
    def download(self, request, pk=None):
        album = self.get_object()

        zip_content = generate_zip(album)

        response = Response(zip_content)
        response['Content-Disposition'] = 'attachment; filename="album.zip"'

        return response
