from django.contrib import admin
from django.utils import timezone

from .models import Category, Post, PostView, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "slug")
    list_filter = (
        "author",
        "category",
        "tags",
        "is_published",
    )

    search_fields = ("title", "content")
    readonly_fields = ["created_at", "published_at", "reading_time"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "author",
                    "title",
                    "category",
                    "tags",
                    "image",
                    "content",
                    "reading_time",
                    "created_at",
                    "published_at",
                )
            },
        ),
        ("Permissions", {"fields": ("is_published",)}),
    )

    @admin.action(description="Mark selected posts as published")
    def make_published(modeladmin, request, queryset):
        for post in queryset:
            post.is_published = True
            post.published_at = timezone.now()
            post.save()

    actions = [make_published]


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    pass
