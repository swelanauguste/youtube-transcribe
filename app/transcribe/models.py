import re
import uuid

import googleapiclient.discovery
import requests
from bs4 import BeautifulSoup
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def get_youtube_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one('meta[property="og:title"]')["content"]
    return title


def get_word_count(words):
    data = words
    word_count = len(data.split())
    return word_count


def get_video_length(video_id):
    api_service_name = "youtube"
    api_version = "v3"
    api_key = (
        "AIzaSyCRZrpkCf1_argyAhaaRTmJqgVjXLfIZ-Y"  # Replace with your actual API key
    )
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    request = youtube.videos().list(part="contentDetails", id=video_id)
    response = request.execute()

    duration_str = response["items"][0]["contentDetails"]["duration"]
    duration_str = duration_str.replace('PT', "").replace("H", ":").replace('M', ":").replace('S', "")
    # Parse the duration string to extract the length in seconds
    # duration = 0
    # time_parts = {"H": 3600, "M": 60, "S": 1}
    # for part in duration_str[2:].split("M"):
    #     for time_unit in time_parts:
    #         if time_unit in part:
    #             duration += int(part.split(time_unit)[0]) * time_parts[time_unit]
    return duration_str


class Transcribe(models.Model):
    url = models.URLField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    video_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    video_len = models.CharField(max_length=20, null=True, blank=True)
    transcribed = models.TextField(blank=True, null=True)
    word_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price_per_word = models.DecimalField(
        decimal_places=5, max_digits=9, default=0.00157
    )
    
    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        pattern = r"(?<=v=)[\w-]+"
        match = re.search(pattern, self.url)
        if match:
            self.video_id = match.group()
            if not self.transcribed:
                transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
                formatter = TextFormatter()
                self.transcribed = formatter.format_transcript(transcript)
                self.title = get_youtube_title(self.url)
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.word_count:
            self.word_count = get_word_count(self.transcribed)
        if not self.video_len:
            self.video_len = get_video_length(self.video_id)
        super(Transcribe, self).save(*args, **kwargs)

    def get_cost_of_transcript(self):
        return self.word_count * self.price_per_word

    def __str__(self):
        if self.title:
            return f"{self.title}"
        if self.video_id:
            return f"{self.video_id}"
        return f"{self.uid}"
