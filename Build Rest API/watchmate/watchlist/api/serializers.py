from rest_framework import serializers

from watchlist.models import StreamPlatform, WatchList


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'stream-detail'}
        }
