from rest_framework import serializers

from .models import Category, Post, Tag


class TagsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name", "slug"]
        read_only_fields = [f for f in fields]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        read_only_fields = [f for f in fields]


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    category = serializers.CharField(source="category.name")
    category_slug = serializers.CharField(source="category.slug")
    post_tags = TagsListSerializer(source="tags", many=True)
    date_display = serializers.SerializerMethodField()
    post_view_count = serializers.IntegerField(source="view_count")

    url = serializers.HyperlinkedIdentityField(
        view_name="api:posts:post-detail", lookup_field="slug"
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "slug",
            "content",
            "image",
            "category",
            "category_slug",
            "post_tags",
            "date_display",
            "url",
            "reading_time",
            "post_view_count",
        ]
        read_only_fields = [f for f in fields]

    def get_date_display(self, obj):
        if obj.published_at:
            return obj.published_at.strftime("%d %B, %Y")
        return obj.created_at.strftime("%d %B")


class PostArchiveReadSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name="api:posts:post-detail", lookup_field="slug"
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "date_display",
            "url",
        ]
        read_only_fields = [f for f in fields]

    def get_date_display(self, obj):
        if obj.published_at:
            return obj.published_at.strftime("%d %B, %Y")
        return obj.created_at.strftime("%d %B")


class PostArchiveSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    posts = PostArchiveReadSerializer(read_only=True, many=True)
