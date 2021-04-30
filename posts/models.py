from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
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


class PostManager(models.Manager):
    pass
    # def total_view_count(self):
    #     view_count = 0
    #     view_count = view_count + 1
    #     return view_count


class Post(models.Model, HitCountMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = RichTextUploadingField(config_name='post_content')
    slug = models.SlugField(max_length=55, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/posts', default='images/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    # object = PostManager()
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

    def total_hit_count(self):  # total views count of product
        return self.hit_count.hits


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
