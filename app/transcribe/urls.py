from django.urls import path

from .views import TranscribeCreateView, TranscribeDetailView, TranscribeListView

urlpatterns = [
    path("list/", TranscribeListView.as_view(), name="trans-list"),
    path(
        "detail/<int:pk>/", TranscribeDetailView.as_view(), name="trans-detail"
    ),
    path("", TranscribeCreateView.as_view(), name="trans-create"),
]
