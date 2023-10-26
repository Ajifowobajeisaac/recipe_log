from django.shortcuts import render

from .models import Recipe_name, Entry

# Create your views here.

def index(request):
    """The home page for Recipe log. """
    return render(request, 'recipe_log/index.html')

def recipes(request):
    """Show all recipe names"""
    recipe_names = Recipe_name.objects.order_by('date_added')
    context = {'recipe_names': recipe_names}
    return render(request,'recipe_log/recipes.html', context)

def recipe(request, recipe_id):
    """Displays individual recipes"""
    recipe = Recipe_name.objects.get(id=recipe_id)
    entry = recipe.entry_set()
    context = {'recipe': recipe, 'entry': entry}
    return render(request, 'recipe_log/recipes/recipe.html', context)
