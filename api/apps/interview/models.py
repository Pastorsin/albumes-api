from django.db import models


class YoutubeVideo(models.Model):

    code = models.URLField()

    thumbnail = models.URLField()


class Interview(models.Model):

    name = models.CharField(max_length=255)

    youtube_video = models.ForeignKey(
        YoutubeVideo,
        on_delete=models.CASCADE
    )
