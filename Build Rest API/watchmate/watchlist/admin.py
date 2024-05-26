from django.contrib import admin

from watchlist.models import StreamPlatform, WatchList

# Register your models here.
admin.site.register(StreamPlatform)
admin.site.register(WatchList)
