import uuid

from django.conf import settings
from django.core.mail import send_mass_mail
from django.db import models

from blog.apps.utils.models import TimestampedModel


class SubscribedUser(models.Model):
    email = models.CharField(unique=True, max_length=50)
    conf_num = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class BaseNewsletter(TimestampedModel):
    """
    BaseModel for Newsletter
    """

    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"{self.subject} {self.created_at.strftime('%B %d, %Y')}"

    class Meta:
        abstract = True


class PostNewsletter(BaseNewsletter):
    """
    create newsletter from post
    """

    post = models.OneToOneField("posts.Post", on_delete=models.CASCADE)

    def send(self, request):
        """
        Send newsletter to all subscribed users
        """
        datatuple = []
        for sub in SubscribedUser.objects.filter(is_active=True):
            mail_tuple = (
                self.subject,
                self.message,
                settings.ADMIN_EMAIL,
                [sub],
            )
            datatuple.append(mail_tuple)

        send_mass_mail(
            datatuple=datatuple, fail_silently=True
        )  # send different mails to each SubscribedUser
