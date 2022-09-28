from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Recipes, Category
from django.utils import timezone
from .forms import PostForm, RecipesForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class AddRecipe(CreateView):
    form_class = RecipesForm
    template_name = 'blog/new_recipe.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление рецепта'
        return context


class Home(ListView):
    model = Recipes
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipes.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваши рецепты'

        return context


class HomeCategory(ListView):
    model = Recipes
    context_object_name = 'recipes'
    model = Category
    allow_empty = False

    def get_queryset(self):
        return Recipes.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['recipes'][0].category)
        context['category_selected'] = context['recipes'][0].category_id
        return context


# Create your views here.

# def home(request, *args, **kwargs):
#     # posts = Post.objects.order_by('published_date')
#     recipes = Recipes.objects.all()
#
#     context = {
#         'recipes': recipes,
#
#         'category_selected': 0
#     }
#     return render(request, "blog/home.html", context=context)


# походу постлист не нужен
# def post_list(request):
#     posts = Post.objects.order_by('published_date')
#     recipes = Recipes.objects.all()
#     return render(request, 'blog/post_list.html', {'recipes': recipes})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

#
# def show_category(request, slug, category_id):
#     recipes = Recipes.objects.filter(category_id=category_id)
#     slug = Category.objects.filter(slug=slug)
#     context = {
#         'recipes': recipes,
#         'slug': slug,
#         'category_selected': category_id
#     }
#     return render(request, "blog/home.html", context=context)
#

class ShowRecipe(DetailView):
    model = Recipes
    #title = "RECIPE"
    template_name = 'blog/show_recipe.html'
    context_object_name = 'recipe'


    def get_page_title(self, context):
        return context["recipe"].title

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['recipe']
        return context


# def show_recipe(request, slug):
#     recipe = get_object_or_404(Recipes, slug=slug)
#     # Post.objects.get(pk=pk)
#     context = {
#         'recipe': recipe,
#         'title': recipe.title,
#         'category_selected': recipe.category_id
#     }
#
#     return render(request, 'blog/show_recipe.html', context=context)


# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})


# def new_recipe(request):
#     if request.method == "POST":
#         # form = PostForm(request.POST)
#         form_recipe = RecipesForm(request.POST)
#         if form_recipe.is_valid():
#             try:
#                 Recipes.objects.create(**form_recipe.cleaned_data)
#                 return redirect('/')
#             except:
#                 form_recipe.add_error(None, 'ОШИБКА')
#             # recipe = form_recipe.save(commit=False)
#             # recipe.cook = request.user
#             #
#             # recipe.save()
#             # return redirect('/', pk=recipe.pk)
#     else:
#         # form = PostForm()
#         form_recipe = RecipesForm()
#     return render(request, 'blog/new_recipe.html', {'form_recipe': form_recipe})


# def user_new(request):


class UpdateRecipe(UpdateView):
    model = Recipes
    context_object_name = 'recipe'
    fields = ['title', 'text', 'category', 'photo']
    template_name = 'blog/recipe_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление рецепта ' + str(context['recipe'])
        return context

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
