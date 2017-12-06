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
    tuna_100g = Ingredient(name='100 g of tuna')
    tuna_100g.save()

    tuna = Product(name='tuna')
    tuna.ingredient = tuna_100g
    tuna.save()

    hundred_grams = Amount(value=100, units=Amount.GRAM)
    hundred_grams.ingredient = tuna_100g
    hundred_grams.save()

    assert(Ingredient.objects.get(name='100 g of tuna').product == tuna)
    assert(Ingredient.objects.get(name='100 g of tuna').amount == hundred_grams)


@pytest.mark.django_db
def test_dish_can_have_many_ingredients():
    tuna_with_chips = Dish(name='tuna_with_chips')
    tuna_with_chips.save()
    tuna_with_chips.ingredient_set.create(name='tuna')
    tuna_with_chips.ingredient_set.create(name='chips')


@pytest.mark.django_db
def test_single_product_can_be_part_of_multiple_ingredients():
    tuna = Product(name='tuna')

    tuna_200g = Ingredient(amount=Amount(value=200, units=Amount.GRAM))
    tuna_200g.product = tuna
    tuna_200g.save()

    tuna_100g = Ingredient(amount=Amount(value=100, units=Amount.GRAM))
    tuna_100g.product = tuna
    tuna_100g.save()

    print(tuna_100g)
    # print(tuna_100g.amount.value)







