from django.urls import path

from .views import comments_list_create
urlpatterns = [
    path('<str:slug>/comments/',comments_list_create, name='comments_list_create'),
    # path('<str:slug>/comments/<int:pk>/', comments_reply, name='comments_reply'),
]
