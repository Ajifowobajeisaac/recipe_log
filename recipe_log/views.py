from django.shortcuts import render, redirect

from .models import Recipe_name, Entry
from .forms import RecipeForm, EntryForm

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
    entry = recipe.entry_set.order_by('date_added')
    context = {'recipe': recipe, 'entry': entry}
    return render(request, 'recipe_log/recipe.html', context)

def new_recipe(request):
    """Add a new recipe"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = RecipeForm()
    else:
        # Post data submitted; process data.
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_log:recipes')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'recipe_log/new_recipe.html', context)

def new_entry(request, recipe_id):
    """Adds a new entry"""
    recipe = Recipe_name.objects.get(id=recipe_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.recipe = recipe
            form.save()
            return redirect('recipe_log:recipe', recipe_id=recipe_id)
        
    # Display a blank or invalid form.
    context = {'recipe' : recipe,'form' : form}
    return render(request, 'recipe_log/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edits a recipe entry"""
    entry = Entry.objects.get(id=entry_id)
    recipe = entry.recipe

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('recipe_log:recipe', entry_id=entry_id)
        
    context = {'entry': entry, 'recipe': recipe, 'form': form}
    return render(request, 'recipe_log:edit_entry.html', context)
