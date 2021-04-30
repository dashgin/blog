from django.db.models import Count

from posts.models import Category, Tag, Post


def c_t_p_list(request):
    categories = Category.objects.annotate(number_of_posts=Count('post'))
    tags = Tag.objects.annotate(number_of_posts=Count('post'))
    all_posts = Post.objects.all().order_by('hit_count_generic')[:3]
    context = {
        'categories': categories,
        'tags': tags,
        'all_posts': all_posts
    }
    return context
