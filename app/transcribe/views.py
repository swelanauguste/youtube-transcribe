from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from youtube_transcript_api import YouTubeTranscriptApi
from django.http import HttpResponseRedirect
from .models import Transcribe
from .forms import AddTranscribeForm
# YouTubeTranscriptApi.get_transcript(video_id)


class TranscribeListView(ListView):
    model = Transcribe


class TranscribeDetailView(DetailView):
    model = Transcribe
    # slug_url_kwarg = "video_id"


class TranscribeCreateView(CreateView):
    model = Transcribe
    form_class = AddTranscribeForm
    
    # def post(self, request, *args, **kwargs):
    #     form = BookCreateForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
    #     return render(request, 'books/book-create.html', {'form': form})
