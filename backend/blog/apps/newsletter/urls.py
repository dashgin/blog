from django.urls import path

from .views import Confirm, Subscribe, Unsubscribe

app_name = "newsletter"
urlpatterns = [
    path("subscribe/<str:email>/", Subscribe.as_view(), name="subscribe"),
    path("confirm/", Confirm.as_view(), name="confirm"),
    path("unsubscribe/<str:email>/", Unsubscribe.as_view(), name="unsubscribe"),
]
