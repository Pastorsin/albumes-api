from django.db import models
from urllib.parse import urlunsplit, urlencode


class YoutubeVideo(models.Model):

    code = models.CharField(max_length=255)

    thumbnail = models.URLField()

    @property
    def url(self):
        PATH = "/watch"
        SCHEME = "https"
        NETLOC = "www.youtube.com"

        query = urlencode(dict(v=self.code))

        return urlunsplit((SCHEME, NETLOC, PATH, query, ""))


class Interview(models.Model):

    name = models.CharField(max_length=255, unique=True)

    youtube_video = models.ForeignKey(
        YoutubeVideo,
        on_delete=models.CASCADE
    )
