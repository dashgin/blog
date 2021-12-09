from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from blog.apps.utils.models import TimestampedModel, get_unique_slug


class TagManager(models.Manager):
    pass


class Tag(models.Model):
    name = models.CharField(_("title"), max_length=250)
    slug = models.CharField(blank=True, max_length=255)

    objects = TagManager()

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class CategoryManager(models.Manager):
    pass


class Category(models.Model):
    name = models.CharField(_("title"), max_length=250)
    slug = models.CharField(blank=True, max_length=255)

    objects = CategoryManager()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class PostView(TimestampedModel):
    ip_address = models.GenericIPAddressField(null=True)
    post = models.ForeignKey("Post", related_name="post_view", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ip_address} in Post: {self.post.title}"


class PostQuerySet(models.QuerySet):
    def by(self, author):
        return self.filter(author__username=author)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.filter(is_published=True)


class Post(TimestampedModel):
    title = models.CharField(_("subject"), max_length=250, db_index=True)
    content = RichTextField(_("content"), config_name="post_content")
    image = models.URLField(_("image url"), null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(_("slug"), max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="post_tags")

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("api:posts:post-detail", kwargs={"slug": self.slug})

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def reading_time(self):
        time = (self.content.count(" ")) // 300
        return f"{time+1} min"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self)
        return super(Post, self).save(*args, **kwargs)
