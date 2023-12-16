from django.test import TestCase
from django.urls import reverse

from accounts.models import User, UserManager
from recipe_log.models import Recipe, RecipeDetails

class TestRecipe(TestCase):
    """Tests the Recipe Model and it's attributes"""

    def test_string_representation(self):
        recipe = Recipe(text="Jollof Rice")
        self.assertEqual(str(recipe), "Jollof Rice")

class TestRecipesView(TestCase):
    """The the views for Recipe"""

    @classmethod
    def setUpTestData(cls):

        #Creates 5 Users for testing
        user_list = []
        for user_id in range(5):
            UserManager.create_user(
                f'tester{user_id}@gmail.com', 
                date_of_birth=f'13-{user_id}-2000'
            )

        #Creates 10 Recipes for testing
        number_of_recipes = 10
        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(text=f'Recipe {recipe_id}')

    def test_view_url_exists_at_right_location(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)   
