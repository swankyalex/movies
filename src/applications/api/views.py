from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions

from applications.api.serializers import ActorDetailSerializer
from applications.api.serializers import ActorListSerializer
from applications.api.serializers import CreateRatingSerializer
from applications.api.serializers import MovieDetailSerializer
from applications.api.serializers import MovieListSerializer
from applications.api.serializers import ReviewCreateSerializer
from applications.api.service import get_client_ip
from applications.api.service import MovieFilter
from applications.api.service import PaginationMovies
from applications.movies.models import Actor
from applications.movies.models import Movie


class MovieApiView(generics.ListAPIView):
    """Вывод списка фильмов"""

    serializer_class = MovieListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationMovies

    def get_queryset(self):
        movies = (
            Movie.objects.filter(draft=False)
            .annotate(
                rating_user=models.Count(
                    "ratings", filter=models.Q(ratings__ip=get_client_ip(self.request))
                )
            )
            .annotate(
                middle_star=models.Sum(models.F("ratings__star"))
                / models.Count(models.F("ratings"))
            )
        ).order_by("id")
        return movies


class MovieDetailApiView(generics.RetrieveAPIView):
    """Вывод фильма"""

    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к фильму"""

    serializer_class = ReviewCreateSerializer


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга фильму"""

    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsListView(generics.ListAPIView):
    """Вывод списка актеров"""

    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsDetailView(generics.RetrieveAPIView):
    """Вывод актера или режиссера"""

    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
