from django import forms
from .models import Post, Recipes


class PostForm(forms.ModelForm):
    """docstring forPostForm."""
    class Meta:
        model = Post
        fields = ('title', 'text')


class RecipesForm(forms.ModelForm):
    """docstring forPostForm."""
    class Meta:
        model = Recipes
        fields = ('title',  'text',  'category')