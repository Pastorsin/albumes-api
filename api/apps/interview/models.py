from django.db import models
from urllib.parse import urlunsplit, urlencode


class YoutubeVideo(models.Model):

    code = models.CharField(max_length=255, unique=True)

    @property
    def url(self):
        PATH = "/watch"
        SCHEME = "https"
        NETLOC = "www.youtube.com"

        query = urlencode(dict(v=self.code))

        return urlunsplit((SCHEME, NETLOC, PATH, query, ""))

    @property
    def thumbnail(self):
        return f"https://i.ytimg.com/vi/{self.code}/maxresdefault.jpg"


class Interview(models.Model):

    name = models.CharField(max_length=255)

    youtube_video = models.OneToOneField(
        YoutubeVideo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
