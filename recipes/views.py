from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipesPage(generic.ListView):
    
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 8