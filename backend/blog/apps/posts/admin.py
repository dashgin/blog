from django.contrib import admin

from .models import Category, Post, PostViews, Tag


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
    readonly_fields = ["created_at", "reading_time"]
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
                    "reading_time"
                    # "created_at",
                    # "updated_at",
                )
            },
        ),
        ("Permissions", {"fields": ("is_published",)}),
    )


admin.site.register(PostViews)
