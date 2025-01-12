from .models import Ad
from .owner import (
    OwnerCreateView,
    OwnerDeleteView,
    OwnerDetailView,
    OwnerListView,
    OwnerUpdateView,
)


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ["title", "text", "price"]


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ["title", "text", "price"]


class AdDeleteView(OwnerDeleteView):
    model = Ad
