from django.views.generic import TemplateView, ListView

from posts.models import Post


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    paginate_by = 2
