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

    def validate(self, data):
        validated_data = super().validate(data)

        interview_name = validated_data["name"]
        video_code = validated_data["youtube_video"]["code"]

        if Interview.exists(interview_name, video_code):
            raise serializers.ValidationError("Interview already exists.")

        return validated_data

    def create(self, validated_data):
        video, _ = YoutubeVideo.objects.get_or_create(
            **validated_data["youtube_video"]
        )

        validated_data["youtube_video"] = video

        return super().create(validated_data)
