from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from blog.utils.models import TimeStampedModel


class BlogUser(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Tag(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class PostViews(TimeStampedModel):
    ip_address = models.GenericIPAddressField(null=True)
    post = models.ForeignKey('Post', related_name='post_views', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip_address} in Post: {self.post.title}'


class Post(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    content = RichTextField(config_name='post_content')
    # content = RichTextUploadingField(config_name='post_content')
    slug = models.SlugField(max_length=55, unique=True, editable=False)
    category = models.ForeignKey(Category, related_name='category_posts', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, related_name='post_tags', )
    image = models.ImageField(upload_to='images/posts', default='images/default.png')
    is_published = models.BooleanField(default=False)

    @property
    def views_count(self):
        return PostViews.objects.filter(post=self).count()

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


class Comment(models.Model):
    author = models.ForeignKey(BlogUser, related_name='blog_user_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comments')  # related_name='post_comment'
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment {self.content} by {self.author.email}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.post.slug})

    def approve(self):
        self.approved_comment = True
        self.save()
