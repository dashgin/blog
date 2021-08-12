from django.contrib import admin

from .models import Category, Tag, Post, Comment, PostViews, BlogUser

admin.site.register(PostViews)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count')
    list_filter = ('author', 'category', 'tags', 'is_published',)
    search_fields = ('title', 'subtitle')
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('author', 'title', 'subtitle', 'category',
                           'tags', 'image', 'content', 'created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_published',)}),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'is_active')
    list_filter = ('post', 'is_active',)


class CommentInlines(admin.TabularInline):
    model = Comment
    fields = ['post', 'content']
    extra = 0


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    inlines = [CommentInlines]
