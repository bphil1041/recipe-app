from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Recipe
from .forms import RecipeForm

User = get_user_model()


class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            description="A delicious pasta dish",
            ingredients="Spaghetti, pasta sauce, ground beef",
            cooking_time=30,
            difficulty="Easy"
        )
        self.assertEqual(str(recipe), "Spaghetti Carbonara")


class RecipeFormTest(TestCase):
    def setUp(self):
        self.recipe_data = {
            'title': 'Test Recipe',
            'description': 'A test recipe description.',
            'ingredients': 'Test ingredients.',
            'cooking_time': 30,
            'difficulty': 'Easy'
        }

    def test_recipe_form_valid(self):
        form = RecipeForm(data=self.recipe_data)
        self.assertTrue(form.is_valid())

    def test_recipe_form_title_max_length(self):
        self.recipe_data['title'] = 'A' * 256  # Exceeding max length
        form = RecipeForm(data=self.recipe_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class RecipeListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='A test recipe description.',
            ingredients='Test ingredients.',
            cooking_time=30,
            difficulty='Easy'
        )


def test_login_required(self):
    response = self.client.get('/recipes/')
    self.assertRedirects(response, '/login/?next=/recipes/')

    def test_recipes_list_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipes_list_view_pagination(self):
        for i in range(15):  # Create more than 10 recipes for pagination
            Recipe.objects.create(
                title=f'Test Recipe {i}',
                description='A test recipe description.',
                ingredients='Test ingredients.',
                cooking_time=30,
                difficulty='Easy'
            )

        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('recipes_list'))
        self.assertEqual(len(response.context['recipes']), 10)


class RecipeDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='A test recipe description.',
            ingredients='Test ingredients.',
            cooking_time=30,
            difficulty='Easy'
        )

    def test_recipe_detail_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(
            reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
