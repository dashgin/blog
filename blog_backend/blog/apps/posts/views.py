from rest_framework import filters, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from .models import Post, Category, Tag, PostViews, Comment, BlogUser
from .serializers import (TagsListSerializer, CategoryListSerializer,
                          PostReadSerializer, CommentSerializer,
                          CategorySerializer, TagSerializer)
from rest_framework.pagination import PageNumberPagination

from collections import OrderedDict


class SimplePagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            # ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'subtitle', 'content']
    order_fields = ['created_at']
    lookup_field = 'slug'
    pagination_class = SimplePagination

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset.filter(is_published=True)
        tags = self.request.GET.getlist(key='tag')
        if tags:
            queryset = queryset.filter(tags__name__in=tags)
        return queryset

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else self.request.META.get('REMOTE_ADDR')
        PostViews.objects.get_or_create(post=obj, ip_address=ip)
        print(obj.views_count)
        return obj

    @action(detail=False, methods=["GET"])
    def most_reads(self, request):
        most_reads_posts = Post.objects.all().order_by('-post_views')[:3]
        serializer = PostReadSerializer(most_reads_posts, many=True, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        if self.action == 'retrieve':
            return CategorySerializer
        return super().get_serializer_class()


class TagViewSet(ListModelMixin, GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return TagsListSerializer
        if self.action == 'retrieve':
            return TagSerializer
        return super().get_serializer_class()


class CommentListCreateAPIView(ListCreateAPIView):
    # parent = get_object_or_404(Comment, pk=int(self.kwargs['pk']))
    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(post__slug=self.kwargs['slug']).filter(is_active=True)
        return queryset

    def get(self, request, *args, **kwargs):
        serializer = CommentSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        context = super(CommentListCreateAPIView, self).get_serializer_context()
        # context.update({"email": self.request.data['email']})
        return context

    def perform_create(self, serializer):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        serializer.save(post_id=post.id)


comments_list_create = CommentListCreateAPIView.as_view()
