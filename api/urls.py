from django.urls import path, include
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CategoryListAPIView, TagListAPIView


urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('tags/', TagListAPIView.as_view())
]
