from django import forms
from django.forms import HiddenInput

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'image', 'category', 'tags', 'is_draft']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'content']
        widgets = {'post': HiddenInput()}
