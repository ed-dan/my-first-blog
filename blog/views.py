from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Recipes, Category
from django.utils import timezone
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Create your views here.


def home(request, *args, **kwargs):
    # posts = Post.objects.order_by('published_date')
    recipes = Recipes.objects.all()
    cats = Category.objects.all()
    context = {
        'recipes': recipes,
        'cats': cats,
        'category_selected': 0
    }
    return render(request, "blog/home.html", context=context)


# походу постлист не нужен
# def post_list(request):
#     posts = Post.objects.order_by('published_date')
#     recipes = Recipes.objects.all()
#     return render(request, 'blog/post_list.html', {'recipes': recipes})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


def show_category(request, category_id):
    recipes = Recipes.objects.filter(category_id=category_id)
    cats = Category.objects.all()
    context = {
        'recipes': recipes,
        'cats': cats,
        'category_selected': category_id
    }
    return render(request, "blog/home.html", context=context)


def show_recipe(request, pk):
    r = get_object_or_404(Recipes, pk=pk)
    # Post.objects.get(pk=pk)

    Recipes.objects.get(pk=pk)
    return render(request, 'blog/show_recipe.html', {'r': r})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def new_recipe(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form_recipe = Recipes(request.POST)
        if form.is_valid():
            form_recipe = form.save(commit=False)
            form_recipe.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# def user_new(request):


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
