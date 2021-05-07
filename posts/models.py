from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=51, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=51, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class PostViews(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip_address} in Post: {self.post.title}'


class PostManager(models.Manager):
    def all(self):
        return Post.objects.filter(is_active=True)

    def get_queryset(self):
        return super(PostManager, self).get_queryset()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    content = RichTextUploadingField(config_name='post_content')
    slug = models.SlugField(max_length=55, unique=True, editable=False)
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, related_name='post_tags', )
    image = models.ImageField(upload_to='images/posts', default='images/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)

    @property
    def views_count(self):
        return PostViews.objects.filter(post=self).count()

    objects = PostManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment by {self.name}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.post.slug})
