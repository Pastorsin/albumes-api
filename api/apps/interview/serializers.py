from interview.models import Interview, YoutubeVideo
import requests
from rest_framework import serializers


class YoutubeCodeValidator():
    MESSAGE = "Code of Youtube video is incorrect."

    def __call__(self, video):
        code = video["code"]

        video_url = f"http://www.youtube.com/watch?v={code}"
        check_url = f"https://www.youtube.com/oembed?url={video_url}"

        response = requests.head(check_url)

        if not response.ok:
            raise serializers.ValidationError(self.MESSAGE)


class YoutubeVideoSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only=True)

    class Meta:
        model = YoutubeVideo
        fields = ['id', 'code', 'thumbnail', 'url']
        validators = [YoutubeCodeValidator()]


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
