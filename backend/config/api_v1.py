from django.urls.conf import include, path

from .swagger_config import urlpatterns as doc_urls

app_name = "api"

urlpatterns = [
    path("", include(doc_urls)),
    path("posts/", include("blog.apps.posts.urls")),
    path("newsletter/", include("blog.apps.newsletter.urls")),
]
