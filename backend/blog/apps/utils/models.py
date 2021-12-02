from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)


def get_unique_slug(model):
    slug = slugify(model.title)
    unique_slug = slug
    counter = 1
    while model.__class__.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1
    return unique_slug
