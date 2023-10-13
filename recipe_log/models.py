from django.db import models

# Create your models here

class Recipe_name(models.Model):
    """The name of the recipe the user entered"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        """Return the string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """The conntent of a recipe"""
    recipe = models.ForeignKey(Recipe_name, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns the string representaion of the entry"""
        return f"{self.text[:50]}..."
