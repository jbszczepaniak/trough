from django.test import TestCase

from trough.main.models import Dish, Ingredient


class TestDishModel(TestCase):
    def setUp(self):
        self.dish = Dish(name='Tuna with chips')

    def test_model_can_create_dish(self):
        old_count = Dish.objects.count()
        self.dish.save()
        new_count = Dish.objects.count()
        self.assertNotEqual(old_count, new_count)


class TestIngredientModel(TestCase):
    def setUp(self):
        self.ingredient_name = 'tuna'
        self.ingredient = Ingredient(name=self.ingredient_name)

    def test_model_can_create_an_ingredient(self):
        self.ingredient.save()
        Ingredient.objects.get(name=self.ingredient_name)
