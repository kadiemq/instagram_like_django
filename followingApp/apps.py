from django.apps import AppConfig


class FollowingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followingApp'

    def ready(self):
        import followingApp.signals
