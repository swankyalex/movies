from django.db import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.api.serializers import ActorDetailSerializer
from applications.api.serializers import ActorListSerializer
from applications.api.serializers import CreateRatingSerializer
from applications.api.serializers import MovieDetailSerializer
from applications.api.serializers import MovieListSerializer
from applications.api.serializers import ReviewCreateSerializer
from applications.api.service import get_client_ip
from applications.movies.models import Actor
from applications.movies.models import Movie


class MovieApiView(APIView):
    """Вывод списка фильмов"""

    def get(self, request):
        movies = (
            Movie.objects.filter(draft=False)
            .annotate(
                rating_user=models.Count(
                    "ratings", filter=models.Q(ratings__ip=get_client_ip(request))
                )
            )
            .annotate(
                middle_star=models.Sum(models.F("ratings__star"))
                / models.Count(models.F("ratings"))
            )
            .order_by("id")
        )
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailApiView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Добавление отзыва к фильму"""

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStarRatingView(APIView):
    """Добавление рейтинга фильму"""

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


class ActorsListView(generics.ListAPIView):
    """Вывод списка актеров"""

    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsDetailView(generics.RetrieveAPIView):
    """Вывод актера или режиссера"""

    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
