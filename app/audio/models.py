from django.db import models
from django.urls import reverse


def user_directory_path(instance, filename):
    return "audio_files".format(instance.user.id, filename)


class AudioTranscription(models.Model):
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
        prefix = "audio-files/"
        if self.audio_file.name.startswith(prefix):
            return f"{self.audio_file.name[len(prefix):]}"
        return f"{self.audio_file.name}"
