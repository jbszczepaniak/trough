import pytest
from django.core.exceptions import ValidationError

from trough.ratings.models import RatingCategory, Rating


@pytest.mark.django_db
def test_rating_has_configurable_categories():
    speed_category = RatingCategory.objects.create(name='Sweets')


def test_rating_can_have_integer_values_from_0_to_10():
    Rating(value=0).full_clean()
    Rating(value=10).full_clean()

    with pytest.raises(ValidationError):
        Rating(value=20).full_clean()
        Rating(value=-2).full_clean()




