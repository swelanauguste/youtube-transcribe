import warnings

from django.db import models
from django.urls import reverse
from numba import jit
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning

warnings.simplefilter("ignore", category=NumbaDeprecationWarning)
warnings.simplefilter("ignore", category=NumbaPendingDeprecationWarning)


# def user_directory_path(instance, filename):
#     return "audio_files".format(instance.user.id, filename)


class AudioTranscription(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, default="processing")
    audio_file = models.FileField(upload_to="audio-files", max_length=255)
    transcript = models.TextField(blank=True)

    def remove_prefix(file_path, prefix):
        if file_path.startswith(prefix):
            return file_path[len(prefix) :]
        return file_path

    @property
    def get_word_count(self):
        data = self.transcript
        word_count = len(data.split())
        return word_count

    @property
    def get_cost_of_transcript(self):
        return self.get_word_count * 0.005

    def get_absolute_url(self):
        return reverse("audio-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"
