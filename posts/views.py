from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, MonthArchiveView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Comment
from .forms import PostCreateForm, CommentForm
from hitcount.views import HitCountDetailView


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


class PostsByCategoryListView(ListView):
    template_name = 'index.html'
    paginate_by = 8
    context_object_name = 'post_list'

    def get_queryset(self, *args, **kwargs):
        posts = Post.objects.filter(category__slug=self.kwargs['slug'])
        return posts


class PostsByTagListView(ListView):
    template_name = 'index.html'
    paginate_by = 8
    context_object_name = 'post_list'

    def get_queryset(self, *args, **kwargs):
        posts = Post.objects.filter(tags__slug=self.kwargs['slug'])
        return posts


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(FormMixin, HitCountDetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    form_class = CommentForm
    count_hit = True

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(slug=self.kwargs['slug'])
        context['comments'] = Comment.objects.filter(post__slug=self.kwargs['slug'])
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'created_at'
    template_name = 'posts/post_archive.html'


class SearchPostListView(ListView):
    template_name = "index.html"
    context_object_name = 'post_list'

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        qs = Post.objects.all()
        if query:
            return qs.filter(
                Q(title__icontains=query) |
                Q(subtitle__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs.none()
