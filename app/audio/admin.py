from django.contrib import admin

from .models import AudioTranscription


@admin.register(AudioTranscription)
class AudioTranscriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']