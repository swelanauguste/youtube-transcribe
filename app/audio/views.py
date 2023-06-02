import whisper
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import AudioTranscriptionForm
from .models import AudioTranscription


class AudioTranscriptionCreateView(CreateView):
    model = AudioTranscription
    form_class = AudioTranscriptionForm

    def post(self, request):
        form = AudioTranscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            transcription = form.save()
            # Perform transcription using OpenAI Whisper
            model = whisper.load_model("base")

            file_path = transcription.audio_file.path
            result = model.transcribe(file_path, fp16=False)
            # with open(file_path, "rb") as f:
            #     file_contents = f.read()
            transcription.transcript = result["text"]
            transcription.save()
            return redirect("audio-detail", pk=transcription.pk)
        return render(request, "audio/audiotranscription_form.html", {"form": form})


class AudioTranscriptionListView(ListView):
    model = AudioTranscription


class AudioTranscriptionDetailView(DetailView):
    model = AudioTranscription
