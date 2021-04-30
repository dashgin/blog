from django.db import models
from django.urls import reverse


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

