from django import forms

from .models import AudioTranscription


class AudioTranscriptionForm(forms.ModelForm):
    class Meta:
        model = AudioTranscription
        fields = (
            "name",
            "audio_file",
        )
