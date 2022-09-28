from django.urls import path
from . import views


urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    # path('', views.home, name='home'),
    # path('recipe/new/', views.new_recipe, name='new_recipe'),
    # path('show_recipe/<slug:slug>/', views.show_recipe, name='show_recipe'),
    # path('category/<slug:slug>/<int:category_id>', views.show_category, name='show_category'),
    # path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('recipe/new/', views.AddRecipe.as_view(), name='new_recipe'),
    path('recipe/<slug:slug>/update', views.UpdateRecipe.as_view(), name='recipe_update'),
    path('', views.Home.as_view(), name='home'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('recipe/<slug:slug>/', views.ShowRecipe.as_view(), name='show_recipe'),
    path('category/<slug:slug>', views.HomeCategory.as_view(), name='show_category')
]
