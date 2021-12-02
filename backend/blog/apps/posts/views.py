from rest_framework import filters, response, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from blog.apps.utils.pagination import SimplePagination

from .models import Category, Post, PostViews, Tag
from .serializers import (
    CategoryListSerializer,
    PostArchiveSerializer,
    PostReadSerializer,
    TagsListSerializer,
)


class TagListAPIView(ListAPIView):
    """Tag List View."""

    serializer_class = TagsListSerializer
    queryset = Tag.objects.all()


tag_list_view = TagListAPIView.as_view()


class CategoryAPIView(ListAPIView):
    """Category List View."""

    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


category_list_view = CategoryAPIView.as_view()


class PostListAPIView(ListAPIView):
    """Post List View."""

    serializer_class = PostReadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "post_views"]
    lookup_field = "slug"
    pagination_class = SimplePagination

    def get_queryset(self):
        # TODO: add filter by tag and category with queryparam
        return Post.objects.published()


post_list_view = PostListAPIView.as_view()


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.published()
    lookup_field = "slug"
    serializer_class = PostReadSerializer

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        ip = (
            x_forwarded_for.split(",")[0]
            if x_forwarded_for
            else self.request.META.get("REMOTE_ADDR")
        )
        PostViews.objects.get_or_create(post=obj, ip_address=ip)
        return obj


post_retrieve_view = PostRetrieveAPIView.as_view()


class PostArchiveAPIView(APIView):
    """
    Return year and post that created in that year.
    """

    serializer_class = PostArchiveSerializer

    def get(self, request, *args, **kwargs):
        dates = Post.objects.published().dates("created_at", "year")
        years = [date.year for date in dates]
        posts = [
            {
                "year": year,
                "posts": Post.objects.published().filter(created_at__year=year),
            }
            for year in years
        ]

        serializer = self.serializer_class(
            posts, many=True, context={"request": request}
        )
        return response.Response(serializer.data, status=status.HTTP_200_OK)


post_archive_view = PostArchiveAPIView.as_view()
