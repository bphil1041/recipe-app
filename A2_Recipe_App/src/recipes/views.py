from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
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


class RecipeListView(LoginRequiredMixin, ListView):
    """Render the list of recipes with optional filtering and pagination."""
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    paginate_by = 10  # Set the number of recipes per page

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
    context = {
        'recipe': recipe,
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
