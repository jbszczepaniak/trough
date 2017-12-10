import pytest

from trough.ratings.models import RatingCategory


@pytest.mark.django_db
def test_rating_has_configurable_categories():
    RatingCategory.objects.create(name='Preparation speed')
