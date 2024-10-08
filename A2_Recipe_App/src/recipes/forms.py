# src/recipes/forms.py

from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description',
                  'ingredients', 'cooking_time', 'difficulty']
