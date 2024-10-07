from django.shortcuts import render
from .models import Recipe  # Import the Recipe model


def home_view(request):
    return render(request, 'recipes/recipes_home.html')


def recipes_list_view(request):
    recipes = Recipe.objects.all()  # Retrieve all recipes from the database
    context = {
        'recipes': recipes,  # Pass the recipes to the template
    }
    return render(request, 'recipes/recipes_list.html', context)


def recipe_detail_view(request, recipe_id):
    # Fetch the recipe by its ID or return a 404 error if not found
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipes/recipe_detail.html', context)
