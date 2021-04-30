from django.urls import path

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    SearchPostListView,
                    PostsByCategoryListView,
                    PostMonthArchiveView,
                    PostsByTagListView
                    )

urlpatterns = [
    path('category/<slug:slug>/', PostsByCategoryListView.as_view(), name='posts-by-category'),
    path('tag/<slug:slug>/', PostsByTagListView.as_view(), name='posts-by-tags'),
    path('', PostListView.as_view(), name='post-list'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    # Example: / 2012 / 08 /
    path('<int:year>/<int:month>/', PostMonthArchiveView.as_view(month_format='%m'),
         name="post-archive"),
    path('search/', SearchPostListView.as_view(), name="search"),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
