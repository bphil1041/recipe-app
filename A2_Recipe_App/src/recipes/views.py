from django.shortcuts import render


def home_view(request):
    return render(request, 'recipes/recipes_home.html')
