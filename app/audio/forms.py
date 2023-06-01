from django import forms

from .models import AudioTranscription


class AudioTranscriptionForm(forms.ModelForm):
    class Meta:
        model = AudioTranscription
        fields = ("audio_file",)
