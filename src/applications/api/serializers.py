from rest_framework import serializers

from applications.movies.models import Movie
from applications.movies.models import Reviews


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


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

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Reviews
        fields = ("name", "text", "children")


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
