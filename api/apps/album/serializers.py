from album.models import Album, Interview
from interview.serializers import InterviewSerializer
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    interviews = InterviewSerializer(many=True, read_only=True)

    interview_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        source='interviews',
        queryset=Interview.objects.all()
    )

    class Meta:
        model = Album
        fields = [
            'id', 'name', 'qr_position', 'interviews', 'interview_ids',
            'created', 'modified'
        ]


class ExportAlbumSerializer(serializers.Serializer):
    file = serializers.FileField(read_only=True)
