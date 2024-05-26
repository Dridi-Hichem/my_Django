from django.http import HttpRequest
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.models import StreamPlatform, WatchList
from watchlist.api.serializers import StreamPlatformSerializer, WatchListSerializer


class StreamPlateformListAV(APIView):
    def get(self, request: HttpRequest) -> Response:
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            platforms, many=True, context={'request': request}
        )

        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        serializer = StreamPlatformSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlateformDetailAV(APIView):
    def get(self, request: HttpRequest, pk: int) -> Response:
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response(
                {"Error": "Stream platform not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)

    def put(self, request: HttpRequest, pk: int) -> Response:
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response(
                {"Error": "Stream platform not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StreamPlatformSerializer(stream_platform, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response(
                {"Error": "Stream platform not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        stream_platform.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
    def get(self, request: HttpRequest) -> Response:
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)

        return Response(serializer.data)

    def post(self, request: HttpRequest) -> Response:
        serializer = WatchListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    def get(self, request: HttpRequest, pk: int) -> Response:
        try:
            movie = WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response(
                {"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request: HttpRequest, pk: int) -> Response:
        try:
            movie = WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response(
                {"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WatchListSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, pk: int) -> Response:
        try:
            movie = WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response(
                {"Error": "Movie not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET", "POST"])
# def movie_list(request: HttpRequest) -> Response:
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request: HttpRequest, pk: int) -> Response:
#     try:
#         movie = Movie.objects.get(pk=pk)

#     except Movie.DoesNotExist:
#         return Response(
#             {"Error": "Movie not found"},
#             status=status.HTTP_404_NOT_FOUND
#         )

#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = MovieSerializer(movie, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
