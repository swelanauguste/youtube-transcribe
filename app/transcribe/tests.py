# from django.test import TestCase

# # Create your tests here.
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import (
    JSONFormatter,
    SRTFormatter,
    TextFormatter,
    WebVTTFormatter,
)

video_id = "BfMSK6GtBFU"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
formatter = WebVTTFormatter()

formatted = formatter.format_transcript(transcript)


print(formatted)
