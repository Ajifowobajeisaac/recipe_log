from django import forms

from .models import Recipe, RecipeDetails

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['text']
        labels = {'text':''}

class RecipeDetailsForm(forms.ModelForm):
    class Meta:
        model = RecipeDetails
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
