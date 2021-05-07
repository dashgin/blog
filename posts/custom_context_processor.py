from django.db.models import Count

from posts.models import Category, Tag, Post


def c_t_p_list(request):
    categories = Category.objects.annotate(number_of_posts=Count('post_category'))
    tags = Tag.objects.filter(post_tags__is_active=True).annotate(number_of_posts=Count('post_tags'))
    all_posts = Post.objects.all().order_by('-postviews')[:3]
    context = {
        'categories': categories,
        'tags': tags,
        'all_posts': all_posts
    }
    return context
