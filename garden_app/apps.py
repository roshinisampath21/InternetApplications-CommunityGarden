from django.apps import AppConfig


class GardenAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "garden_app"
    def ready(self):
        import garden_app.signals
