from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from posts.models import Post
from .forms import ContactForm


class ContactView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/contact'
    success_message = 'Your message has been accepted'

