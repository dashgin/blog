from django.contrib import admin

from posts.models import Category, Tag, Post, Comment, PostViews

admin.site.register(PostViews)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'views_count')
    list_filter = ('author', 'category', 'tags', 'is_active',)
    search_fields = ('title', 'subtitle')
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('author', 'title', 'subtitle', 'category',
                           'tags', 'image', 'content', 'created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_active', 'is_draft')}),
    )

    # def formatted_hit_count(self, obj):
    #     return obj.total_hit_count() if obj.total_hit_count() > 0 else '-'
    #
    # formatted_hit_count.admin_order_field = 'hit_count'
    # formatted_hit_count.short_description = 'Hits'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'is_active')
    list_filter = ('post', 'email', 'is_active',)
