from django.contrib import admin
from .models import Recipe
# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('recipe_name', 'cook', 'status', 'created_on')
    search_fields = ['recipe_name', 'content']
    prepopulated_fields = {'slug': ('recipe_name',)}
    list_filter = ('cook', 'created_on')

    
