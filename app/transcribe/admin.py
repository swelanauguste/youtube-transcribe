from django.contrib import admin

from .models import Transcribe


@admin.register(Transcribe)
class TranscribeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "video_id",
        "url",
        "price_per_min",
        "get_cost_of_transcript",
    ]
