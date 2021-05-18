from album.models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['name', 'qr_position', 'interviews']
        depth = 1
