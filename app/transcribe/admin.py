from django.contrib import admin

from .models import Transcribe

@admin.register(Transcribe)
class TranscribeAdmin(admin.ModelAdmin):
    list_display = ['video_id', 'url']