from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            description="A delicious pasta dish",
            ingredients="Spaghettie, pasta sauce, ground beef",
            cooking_time=30,
            difficulty="Easy"
        )
        self.assertEqual(str(recipe), "Spaghetti Carbonara")
