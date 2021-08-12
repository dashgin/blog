from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from .swagger import urlpatterns as doc_urls
from blog.apps.users.views import UserViewSet
from blog.apps.posts.views import PostViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("categories", CategoryViewSet)
router.register("tags", TagViewSet)

app_name = "api"

urlpatterns = [
    path("", include(doc_urls)),
    path("", include(router.urls)),
    path('posts/', include('blog.apps.posts.urls')),
    path('users/', include('blog.apps.users.urls')),

    # DRF auth token
    # from rest_framework.authtoken.views import obtain_auth_token
    # path('auth-token/', obtain_auth_token),
]
