from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404

from .models import Recipe, RecipeDetails
from .forms import RecipeForm, RecipeDetailsForm

# Create your views here.

def index(request):
    """The home page for Recipe log. """
    return render(request, 'recipe_log/index.html')

@login_required
def recipes(request):
    """Show all recipe names"""
    recipes = Recipe.objects.filter(owner=request.user).order_by('date_added')
    context = {'recipes': recipes}
    return render(request,'recipe_log/recipes.html', context)

@login_required
def recipe(request, recipe_id):
    """Displays individual recipes"""
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404
    # Ensures the recipe belong to the current user.
    if recipe.owner != request.user:
        raise Http404    
    recipe_details = recipe.recipedetails_set.order_by('date_added')
    context = {'recipe': recipe, 'recipe_details': recipe_details}
    return render(request, 'recipe_log/recipe.html', context)

@login_required
def new_recipe(request):
    """Add a new recipe"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RecipeForm()
    else:
        # Post data submitted; process data.
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            new_recipe_name = form.save(commit=False)
            new_recipe_name.owner = request.user
            new_recipe_name.save()
            return redirect('recipe_log:recipes')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'recipe_log/new_recipe.html', context)

@login_required
def new_recipe_details(request, recipe_id):
    """Adds new recipe details"""
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.owner != request.user:
        raise Http404     
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RecipeDetailsForm()
    else:
        # Post data submitted; process data.
        form = RecipeDetailsForm(data=request.POST)
        if form.is_valid():
            new_recipe_details = form.save(commit=False)
            new_recipe_details.recipe = recipe
            form.save()
            return redirect('recipe_log:recipe', recipe_id=recipe_id)
        
    # Display a blank or invalid form.
    context = {'recipe' : recipe,'form' : form}
    return render(request, 'recipe_log/new_recipe_details.html', context)

@login_required
def edit_recipe_details(request, recipe_details_id):
    """Edits the recipe details"""
    recipe_details = RecipeDetails.objects.get(id=recipe_details_id)
    recipe = recipe_details.recipe
    # Ensures the recipe belong to the current user.
    if recipe.owner != request.user:
        raise Http404    

    if request.method != 'POST':
        form = RecipeDetailsForm(instance=recipe_details)
    else:
        form = RecipeDetailsForm(instance=recipe_details, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('recipe_log:recipe', recipe_id=recipe.id)
        
    context = {'recipe_details': recipe_details, 'recipe': recipe, 'form': form}
    return render(request, 'recipe_log/edit_recipe_details.html', context)

@login_required
def delete_recipe(request, recipe_id):
    """Deletes a recipe"""
    to_delete = get_object_or_404(Recipe, pk=recipe_id)
    
    if to_delete.owner != request.user:
        raise PermissionDenied
    
    to_delete.delete()
    return redirect('recipe_log/recipes.html')
