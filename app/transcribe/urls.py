from django.urls import path

from .views import TranscribeCreateView, TranscribeDetailView, TranscribeListView

urlpatterns = [
    path("list/", TranscribeListView.as_view(), name="list"),
    path(
        "detail/<slug:slug>/", TranscribeDetailView.as_view(), name="detail"
    ),
    path("", TranscribeCreateView.as_view(), name="create"),
]
