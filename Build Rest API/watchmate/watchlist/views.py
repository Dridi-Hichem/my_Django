# from django.http import HttpRequest, JsonResponse

# from watchlist.models import Movie

# # Create your views here.
# def movie_list(request: HttpRequest) -> JsonResponse:
#     movies = Movie.objects.all()
#     return JsonResponse(
#         {"movies": list(movies.values())},
#         safe=False
#     )


# def movie_detail(request: HttpRequest, pk: int):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active
#     }

#     return JsonResponse(data)
