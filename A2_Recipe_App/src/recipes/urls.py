# urls.py

from django.urls import path
from .views import home_view, recipes_list_view, recipe_detail_view, login_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),  # Homepage
    path('login/', login_view, name='login'),  # Login URL
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('recipes/', recipes_list_view, name='recipes_list'),  # Recipes list view
    path('recipes/<int:recipe_id>/', recipe_detail_view,
         name='recipe_detail'),  # Recipe detail URL

]
