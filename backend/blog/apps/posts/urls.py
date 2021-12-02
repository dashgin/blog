from django.urls import path

from .views import (
    category_list_view,
    post_archive_view,
    post_list_view,
    post_retrieve_view,
    tag_list_view,
)

app_name = "posts"
urlpatterns = [
    path("", post_list_view, name="post-list"),
    path("tags/", tag_list_view, name="tag-list"),
    path("categories/", category_list_view, name="category-list"),
    path("archive/", post_archive_view, name="post-archive"),
    path("<str:slug>/", post_retrieve_view, name="post-detail"),
]
