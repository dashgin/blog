from django.conf import settings
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("auth-token/", obtain_auth_token),
]

urlpatterns += router.urls
