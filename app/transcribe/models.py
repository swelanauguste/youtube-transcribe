import re
import uuid
from urllib.request import urlopen
import simplejson
from django.db import models
from django.urls import reverse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


class Transcribe(models.Model):
    url = models.URLField("", unique=True)
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    video_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    transcribed = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("trans-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        pattern = r"(?<=v=)[\w-]+"
        match = re.search(pattern, self.url)
        if match:
            self.video_id = match.group()
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
            formatter = TextFormatter()
            self.transcribed = formatter.format_transcript(transcript)
        super(Transcribe, self).save(*args, **kwargs)

    def __str__(self):
        if self.video_id:
            return f"{self.video_id}"
        return f"{self.uid}"
