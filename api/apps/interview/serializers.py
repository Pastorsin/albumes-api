from interview.models import Interview, YoutubeVideo
from rest_framework import serializers


class YoutubeVideoSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only=True)

    class Meta:
        model = YoutubeVideo
        fields = ['id', 'code', 'thumbnail', 'url']


class InterviewSerializer(serializers.ModelSerializer):
    youtube_video = YoutubeVideoSerializer()

    class Meta:
        model = Interview
        fields = ['id', 'name', 'youtube_video']

    def create(self, validated_data):
        video_data = validated_data["youtube_video"]
        video = YoutubeVideo.objects.create(**video_data)

        validated_data.update({"youtube_video": video})
        interview = Interview.objects.create(**validated_data)

        return interview
