from rest_framework import serializers
from posts.models import Category, Tag, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']


class PostSerializer(serializers.ModelSerializer):

    # category = CategorySerializer()
    # tags = TagSerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'subtitle', 'content', 'image', 'slug', 'is_draft', 'created_at']
