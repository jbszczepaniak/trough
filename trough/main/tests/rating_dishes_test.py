import pytest

from trough.main.models import Dish


@pytest.mark.django_db
def test_dish_can_have_couple_rating_categories():
    dish = Dish.objects.create(name='tuna with chips')
    dish.rating_categories.create(name='fish dishes')
    dish.rating_categories.create(name='dinners')

    assert(dish.rating_categories.all().count() == 2)
