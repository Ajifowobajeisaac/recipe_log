from django.shortcuts import render

from .models import Recipe_name

# Create your views here.

def index(request):
    """The home page for Recipe log. """
    return render(request, 'recipe_log/index.html')

def recipes(request):
    """Show all recipe names"""
    recipe_names = Recipe_name.objects.order_by('date_added')
    context = {'recipe_names': recipe_names}
    return render(request,'recipe_log/recipes.html', context)
