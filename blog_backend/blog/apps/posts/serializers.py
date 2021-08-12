from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Post, Category, Tag, Comment, BlogUser


class BlogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = '__all__'


class TagsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        read_only_fields = [f for f in fields]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        read_only_fields = [f for f in fields]


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    category = serializers.CharField(source='category.name')
    post_tags = TagsListSerializer(source='tags', many=True)
    date_display = serializers.SerializerMethodField()
    post_views_count = serializers.IntegerField(source='views_count')

    url = serializers.HyperlinkedIdentityField(
        view_name='api:post-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = [
            'id','author', 'title', 'slug', 'subtitle', 'content', 'image',
            'category', 'post_tags', 'post_views_count',
            'date_display', 'url'
        ]
        read_only_fields = [f for f in fields]

    def get_date_display(self, obj):
        return obj.created_at.strftime("%d %B, %Y")


class CategorySerializer(serializers.ModelSerializer):
    category_posts = serializers.ListSerializer(child=PostReadSerializer())

    class Meta:
        model = Category
        fields = ['name', 'slug', 'category_posts']


class TagSerializer(serializers.ModelSerializer):
    post_tags = serializers.ListSerializer(child=PostReadSerializer())

    class Meta:
        model = Tag
        fields = ['name', 'slug', 'post_tags']


class CommentSerializer(serializers.ModelSerializer):
    # parent_id = serializers.CharField(write_only=True, required=False)
    time_since = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()
    did_replied = serializers.SerializerMethodField()
    author_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Comment
        fields = [
            'post_id', 'content', 'author_email',
            'time_since', 'date_display', 'did_replied'
        ]
        read_only_fields = [
            'time_since', 'date_display', 'did_replied'
        ]

    def create(self, validated_data):
        author_email = validated_data['author_email']
        a, _ = BlogUser.objects.get_or_create(email=author_email)
        post_id = validated_data['post_id']
        post = Post.objects.get(id=post_id)
        content = validated_data['content']
        instance = Comment.objects.create(post=post, author=a, content=content)
        return instance

    def get_time_since(self, obj):
        return timesince(obj.created_at)

    def get_date_display(self, obj):
        return obj.created_at.strftime("%I:%M %p · %d %b %y")

    def get_did_replied(self, obj):
        if obj.parent is not None:
            return True
        return False

    # did_like = serializers.SerializerMethodField()
    # likes_count = serializers.SerializerMethodField()
    # def get_likes_count(self, obj):
    #     return obj.likes.all().count()

    # def get_did_like(self, obj):
    #     request = self.context.get("request")
    #     user = request.user
    #     if user.is_authenticated:
    #         if user in obj.likes.all():
    #             return True
    #     return False
