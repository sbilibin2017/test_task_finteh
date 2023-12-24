from django.apps import AppConfig as DjangoAppConfig  # type: ignore


class AppConfig(DjangoAppConfig):  # type: ignore
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "app"  # type: ignore
