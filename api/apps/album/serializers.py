from album.models import Album
from interview.serializers import InterviewSerializer
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    interviews = InterviewSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'qr_position', 'interviews']


class ExportAlbumSerializer(serializers.Serializer):
    file = serializers.FileField(read_only=True)
