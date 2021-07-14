from django.db import models
from urllib.parse import urlunsplit, urlencode


class YoutubeVideo(models.Model):

    code = models.CharField(max_length=255)

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

    youtube_video = models.ForeignKey(
        YoutubeVideo,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["name", "youtube_video"]

    @classmethod
    def exists(cls, interview_name, video_code):
        interview = cls.objects.filter(
            name=interview_name,
            youtube_video__code=video_code
        )

        return interview.exists()

    def __str__(self):
        return self.name
