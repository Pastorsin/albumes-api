from interview.models import Interview, YoutubeVideo
from rest_framework import serializers


class YoutubeVideoSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only=True)

    class Meta:
        model = YoutubeVideo
        fields = ['code', 'thumbnail', 'url']


class InterviewSerializer(serializers.ModelSerializer):
    youtube_video = YoutubeVideoSerializer()

    class Meta:
        model = Interview
        fields = ['id', 'name', 'youtube_video']
