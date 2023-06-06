import whisper
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import AudioTranscriptionForm
from .models import AudioTranscription
from .tasks import process_transcription


class AudioTranscriptionCreateView(CreateView):
    model = AudioTranscription
    form_class = AudioTranscriptionForm

    def post(self, request):
        form = AudioTranscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()  # Save the form to create a new TranscriptionJob
            process_transcription.delay(
                job.id
            )  # Start the transcription process asynchronously
            return redirect("audio-list")
        return render(request, "audio/audiotranscription_form.html", {"form": form})


class AudioTranscriptionListView(ListView):
    model = AudioTranscription


class AudioTranscriptionDetailView(DetailView):
    model = AudioTranscription
