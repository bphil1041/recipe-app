from django.shortcuts import render
from .models import Recipe  # Import the Recipe model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the protected view
                return redirect('recipes_list')
    else:
        form = AuthenticationForm()
    # Update the template path to include 'recipes'
    return render(request, 'recipes/login.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to logout success page
    return render(request, 'recipes/success.html')
