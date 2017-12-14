from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingCategory(models.Model):
    name = models.CharField(max_length=255, null=True)


class Rating(models.Model):
    value = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ]
    )
