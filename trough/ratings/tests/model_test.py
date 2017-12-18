import pytest
from django.core.exceptions import ValidationError

from trough.ratings.models import RatingCategory, Rating


def test_rating_category_is_printable():
    rc = RatingCategory(name='Sweets')
    assert(rc.__str__() == 'Sweets')


@pytest.mark.django_db
def test_rating_category_has_several_categories():
    sweets_ratings = RatingCategory.objects.create(name='Sweets')
    sweets_ratings.ratings.create(name='sweetness', value=10)
    sweets_ratings.ratings.create(name='bitterness', value=0)

    assert(sweets_ratings.ratings.count() == 2)


def test_rating_can_have_integer_values_from_0_to_10():
    Rating(name='sweetness', value=0).full_clean()
    Rating(name='sweetness', value=10).full_clean()

    with pytest.raises(ValidationError):
        Rating(name='sweetness', value=20).full_clean()
        Rating(name='sweetness', value=-2).full_clean()
