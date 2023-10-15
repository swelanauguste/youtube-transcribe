from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import AddTranscribeForm
from .models import Transcribe


class TranscribeListView(ListView):
    model = Transcribe


class TranscribeDetailView(DetailView):
    model = Transcribe


# def get_video_id(url):
#     pattern = r"(?<=v=)[\w-]+"
#     match = re.search(pattern, url)
#     if match:
#         video_id = match.group()
#     return video_id


class TranscribeCreateView(SuccessMessageMixin, CreateView):
    model = Transcribe
    form_class = AddTranscribeForm

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)
