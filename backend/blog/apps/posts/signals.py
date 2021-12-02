from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.apps.newsletter.models import PostNewsletter

from .models import Post


@receiver(post_save, sender=Post)
def create_newsletter_from_post(sender, instance, created, **kwargs):

    if created:
        PostNewsletter.objects.create(
            subject=f"New post on blog about {instance.title}",
            message=f"{instance.content[:120]} <a href={instance.get_absolute_url()}>Read More</a",
            post=instance,
        )
        print(f"New post on blog about {instance.title}")
    else:
        print("Post was updated")
        pass
