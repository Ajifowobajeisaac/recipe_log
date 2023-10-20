from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Recipe log. """
    return render(request, 'recipe_log/index.html')
