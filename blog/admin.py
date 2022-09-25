from django.contrib import admin
from .models import Post, Recipes, Category


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id', 'category_id')
    list_filter = ['category_id']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


#admin.site.register(Post)
admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category,CategoryAdmin)
