from django import forms
from django.forms import TextInput

from .models import Transcribe


class AddTranscribeForm(forms.ModelForm):
    class Meta:
        model = Transcribe
        fields = ["url"]

        widgets = {
            "url": TextInput(
                attrs={
                    "class": "rounded-pill py-2 shadow",
                }
            )
        }
        labels = {
            "url": "",
        }