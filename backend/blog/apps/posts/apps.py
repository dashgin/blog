from django.apps import AppConfig
from django.conf import settings


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog.apps.posts"

    def ready(self):
        if settings.DEBUG:
            print(">DEBUG::loading_signals")
        import blog.apps.posts.signals  # noqa
