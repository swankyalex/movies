from django.apps import AppConfig


class ApiConfig(AppConfig):
    label = "api"
    name = f"applications.{label}"
    verbose_name = "API"
