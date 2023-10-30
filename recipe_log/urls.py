"""Defines URL patterns for recipe_log"""

from django.urls import path

from . import views

app_name = 'recipe_log'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all the recipe names.
    path('recipes/', views.recipes, name='recipes'),
    # Page that shows an individual recipe.
    path('recipes/<int:recipe_id>/', views.recipe, name='recipe'),
    # Page for adding new recipes.
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    # Page for adding new entries.
    path('new_entry/<int:recipe_id>/', views.new_entry, name='new_entry'),
    # Page for editing entries.
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
    ]
    