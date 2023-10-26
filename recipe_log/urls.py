"""Defines URL patterns for recipe_log"""

from django.urls import path

from . import views

app_name = 'recipe_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the recipe names
    path('recipes/', views.recipes, name='recipes'),
    # Page that shows an individual recipe
    path('recipes/<int:recipe_id>/', views.recipe, name='recipe')
    ]
