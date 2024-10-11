from django.urls import path
# Import the individual views
from .views import home_view, RecipeListView, recipe_detail_view, login_view, logout_view, about_view, signup, profile_view, add_recipe

urlpatterns = [
    path('', home_view, name='home'),  # Homepage
    path('login/', login_view, name='login'),  # Login URL
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('recipes/', RecipeListView.as_view(),
         name='recipes_list'),  # Recipes list view
    path('recipes/<int:recipe_id>/', recipe_detail_view,
         name='recipe_detail'),  # Recipe detail URL
    path('about/', about_view, name='about'),  # About Me page
    path('signup/', signup, name='signup'),  # Sign-up URL
    path('profile/', profile_view, name='profile'),  # Profile page URL
    path('recipes/add/', add_recipe, name='add_recipe'),  # Add recipe page
]
