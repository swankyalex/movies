from django.apps import AppConfig


class ContactConfig(AppConfig):
    label = "contact"
    name = f"applications.{label}"
    verbose_name = "Контакты"
