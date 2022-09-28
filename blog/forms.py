from django import forms
from .models import Post, Recipes


class PostForm(forms.ModelForm):
    """docstring forPostForm."""

    class Meta:
        model = Post
        fields = ('title', 'text')


class RecipesForm(forms.ModelForm):
    """docstring forPostForm."""
    title = forms.CharField(max_length=100, label='ЗАГОЛОВОК')

    class Meta:
        model = Recipes
        fields = ('title', 'slug', 'photo', 'text', 'is_published', 'category')
