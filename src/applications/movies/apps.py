from django.apps import AppConfig


class MoviesConfig(AppConfig):
    label = "movies"
    name = f"applications.{label}"
    verbose_name = "Фильмы"
