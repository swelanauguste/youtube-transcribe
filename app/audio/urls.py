from django.urls import path

from .views import (
    AudioTranscriptionCreateView,
    AudioTranscriptionDetailView,
    AudioTranscriptionListView,
)

urlpatterns = [
    path("", AudioTranscriptionCreateView.as_view(), name="audio-create"),
    path("result/", AudioTranscriptionListView.as_view(), name="audio-list"),
    path(
        "detail/<int:pk>/", AudioTranscriptionDetailView.as_view(), name="audio-detail"
    ),
]
