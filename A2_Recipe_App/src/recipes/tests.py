from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeForm, SignUpForm

# Sample data for testing


def create_recipe(title="Test Recipe", description="Test Description", ingredients="ingredient1, ingredient2", cooking_time=30, difficulty="Easy"):
    return Recipe.objects.create(
        title=title,
        description=description,
        ingredients=ingredients,
        cooking_time=cooking_time,
        difficulty=difficulty
    )


class RecipeListViewTest(TestCase):
    """Test the RecipeListView with and without filters."""

    def setUp(self):
        """Create a user and some test recipes."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.recipe1 = create_recipe(title="Recipe 1", difficulty="Medium")
        self.recipe2 = create_recipe(title="Recipe 2", difficulty="Hard")
        self.recipe3 = create_recipe(title="Recipe 3", difficulty="Easy")

    def test_recipe_list_view(self):
        """Test that the recipe list view loads and displays the recipes."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe1.title)
        self.assertContains(response, self.recipe2.title)

    def test_recipe_list_view_filtering(self):
        """Test filtering recipes by title."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('recipes_list') + '?search=Recipe 1')
        self.assertContains(response, self.recipe1.title)
        self.assertNotContains(response, self.recipe2.title)


class RecipeDetailViewTest(TestCase):
    """Test the recipe detail view."""

    def setUp(self):
        """Create a user and a test recipe."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.recipe = create_recipe()

    def test_recipe_detail_view(self):
        """Test that the recipe detail view works and displays the recipe."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, "ingredient1")


class SignUpViewTest(TestCase):
    """Test the user signup view."""

    def test_signup_view(self):
        """Test that the signup form is rendered and works."""
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword',
            'password2': 'strongpassword'
        })
        # Should redirect after successful signup
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())


class LoginViewTest(TestCase):
    """Test the user login view."""

    def setUp(self):
        """Create a test user."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")

    def test_login_view(self):
        """Test that a user can log in successfully."""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)


class AddRecipeViewTest(TestCase):
    """Test the add recipe view."""

    def setUp(self):
        """Create a test user."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")

    def test_add_recipe_view(self):
        """Test that a user can add a recipe successfully."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_recipe'), {
            'title': 'Test Recipe',
            'description': 'Test Description',
            'ingredients': 'ingredient1, ingredient2',
            'cooking_time': 45,
            'difficulty': 'Medium',
        })
        # Should redirect to profile after adding
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Recipe.objects.filter(title="Test Recipe").exists())
