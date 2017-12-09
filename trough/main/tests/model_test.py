from django.test import TestCase
import pytest
from trough.main.models import Dish, Ingredient, Product, Amount


class TestDishModel(TestCase):
    def setUp(self):
        self.dish = Dish(name='Tuna with chips')

    def test_model_can_create_dish(self):
        old_count = Dish.objects.count()
        self.dish.save()
        new_count = Dish.objects.count()
        self.assertNotEqual(old_count, new_count)


@pytest.mark.django_db
def test_ingredient_has_product_and_value():
    tuna = Product(name='tuna')
    tuna.save()
    hundred_grams = Amount(value=100, units=Amount.GRAM)
    hundred_grams.save()
    Ingredient.objects.create(
        product=tuna,
        amount=hundred_grams,
    ).save()

    ingredient = Ingredient.objects.get(pk=1)
    assert(ingredient.product == tuna)
    assert(ingredient.amount == hundred_grams)


@pytest.mark.django_db
def test_single_product_can_be_part_of_multiple_ingredients():
    tuna = Product(name='tuna')
    tuna.save()

    grams200 = Amount(value=200, units=Amount.GRAM)
    grams100 = Amount(value=100, units=Amount.GRAM)
    grams200.save()
    grams100.save()

    tuna_100g = Ingredient(product=tuna, amount=grams100)
    tuna_100g.save()
    tuna_200g = Ingredient(product=tuna, amount=grams200)
    tuna_200g.save()

    assert(tuna_100g.product == tuna)
    assert(tuna_200g.product == tuna)