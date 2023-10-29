from django import forms

from .models import Recipe_name, Entry

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe_name
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.Modelform):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols:80'})}
