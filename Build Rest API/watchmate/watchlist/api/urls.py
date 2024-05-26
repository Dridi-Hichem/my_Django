from django.urls import path

from watchlist.api.views import StreamPlateformDetailAV, StreamPlateformListAV, WatchListAV, WatchDetailAV

urlpatterns = [
    path("stream/", StreamPlateformListAV.as_view(), name="stream"),
    path("stream/<int:pk>/", StreamPlateformDetailAV.as_view(), name="stream-detail"),
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
]
