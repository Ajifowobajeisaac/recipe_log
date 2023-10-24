"""Defines URL patterns for recipe_log"""

from django.urls import path

from . import views

app_name = 'recipe_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the recipe names
    path('recipe/', views.recipe_names, name='recipe'),
    ]
