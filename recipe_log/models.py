from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Recipe(models.Model):
    """The name of the recipe the user entered"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the model"""
        return self.text
    
class RecipeDetails(models.Model):
    """The conntent of a recipe"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'recipe_details'

    def __str__(self):
        """Returns the string representaion of the entry"""
        return f"{self.text[:50]}..."

class Ingredients(models.Model):
    """The conntent of a recipe"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        """Returns the string representaion of the entry"""
        return f"{self.text[:50]}..."
