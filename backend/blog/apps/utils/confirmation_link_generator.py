from django.urls import reverse
from django.contrib.sites.models import Site

def generate_confirmation_link(user):
    """
    Generates a confirmation link for a user.
    """
    site = Site.objects.get_current()

    return f'{site.domain}{reverse("api:newsletter:confirm")}?email={user.email}&conf_num={user.conf_num}'