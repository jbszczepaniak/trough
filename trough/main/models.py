from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, default=None, null=True)
