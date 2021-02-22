from rest_framework import serializers

from applications.movies.models import Movie
from applications.movies.models import Reviews


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Reviews
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""

    class Meta:
        model = Reviews
        fields = ("name", "text", "parent")


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        exclude = ("draft",)
