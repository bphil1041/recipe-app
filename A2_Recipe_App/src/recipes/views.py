from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.views.generic import ListView
from .models import Recipe
import pandas as pd
import matplotlib.pyplot as plt


def home_view(request):
    """Render the home page for the recipes app."""
    return render(request, 'recipes/recipes_home.html')


def about_view(request):
    """Render the About Me page."""
    return render(request, 'recipes/about_me.html')


class RecipeListView(LoginRequiredMixin, ListView):
    """Render the list of recipes with optional filtering and pagination."""
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        """Filter recipes based on the search query."""
        search_query = self.request.GET.get('search', '')
        queryset = Recipe.objects.all()
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(ingredients__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        """Add DataFrame and search query to context."""
        context = super().get_context_data(**kwargs)
        df = pd.DataFrame(list(context['recipes'].values()))
        context['data_frame'] = df.to_html(classes='table table-striped')
        context['search_query'] = self.request.GET.get('search', '')
        return context


def recipe_detail_view(request, recipe_id):
    """Render the detail view for a specific recipe."""
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Split ingredients into a list if stored as a comma-separated string
    ingredients = recipe.ingredients.split(',') if recipe.ingredients else []

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipes/recipe_detail.html', context)


def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes_list')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    return render(request, 'recipes/success.html')


def visualize_recipes():
    """Create a bar chart visualizing the number of recipes by difficulty."""
    difficulty_counts = Recipe.objects.values(
        'difficulty').annotate(count=Count('id'))
    difficulties = [item['difficulty'] for item in difficulty_counts]
    counts = [item['count'] for item in difficulty_counts]

    plt.figure(figsize=(10, 6))
    plt.bar(difficulties, counts, color='teal')
    plt.xlabel('Difficulty')
    plt.ylabel('Number of Recipes')
    plt.title('Recipes by Difficulty')
    # Save the figure if needed
    plt.savefig('static/recipes_by_difficulty.png')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            # Redirect to the homepage or a welcome page
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'recipes/signup.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Important to keep the user logged in after password change
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'recipes/profile.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Link the recipe to the logged-in user
            recipe.save()
            return redirect('profile')
    else:
        form = RecipeForm()

    # Get the logged-in user's recipes
    recipes = Recipe.objects.filter(user=request.user)

    return render(request, 'profile.html', {'form': form, 'recipes': recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            # Redirect to profile or a list of recipes after saving
            return redirect('profile')
    else:
        form = RecipeForm()

    return render(request, 'recipes/create.html', {'recipe_form': form})
