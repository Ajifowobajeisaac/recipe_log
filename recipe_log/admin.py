from django.contrib import admin

# Register your models here.

from .models import Recipe, RecipeDetails

admin.site.register(Recipe)
admin.site.register(RecipeDetails)
