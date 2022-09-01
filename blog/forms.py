from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """docstring forPostForm."""
    class Meta:
        model = Post
        fields = ('title', 'text')


