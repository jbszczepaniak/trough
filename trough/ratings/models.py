from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingCategory(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ]
    )
    rating_category = models.ForeignKey(
        RatingCategory,
        on_delete=models.CASCADE,
        related_name='ratings',
        blank=True,
        null=True
    )
