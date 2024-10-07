# urls.py

from django.urls import path
from .views import home_view, recipes_list_view, recipe_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/', recipes_list_view, name='recipes_list'),
    path('recipes/<int:recipe_id>/', recipe_detail_view,
         name='recipe_detail'),  # Recipe detail URL
]
