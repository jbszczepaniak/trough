from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False)
