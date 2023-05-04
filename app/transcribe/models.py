import re
import uuid

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


class Transcribe(models.Model):
    url = models.URLField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    video_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    transcribed = models.TextField(blank=True, null=True)
    word_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price_per_word = models.DecimalField(decimal_places=5, max_digits=9, default=0.04)

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

        super(Transcribe, self).save(*args, **kwargs)
        
    def get_cost_of_transcript(self):
        return self.word_count * self.price_per_word

    def __str__(self):
        if self.title:
            return f"{self.title}"
        if self.video_id:
            return f"{self.video_id}"
        return f"{self.uid}"
