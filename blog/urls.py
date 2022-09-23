from django.urls import path
from . import views
from .views import show_category

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('', views.home, name='home'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('show_recipe/<int:pk>/', views.show_recipe, name='show_recipe'),
    path('category/<int:category_id>/', views.show_category, name='show_category'),

]
