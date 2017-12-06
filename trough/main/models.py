from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, null=True)


class Amount(models.Model):
    GRAM = 0
    UNITS_CHOICES = (
        (GRAM, 'Gram'),
    )
    value = models.IntegerField(null=True)
    units = models.IntegerField(null=True, choices=UNITS_CHOICES, default=GRAM)
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, null=True)


