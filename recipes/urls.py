from . import views
from django.urls import path

urlpatterns = [
    path('recipes', views.RecipesPage.as_view(), name='recipes')
]