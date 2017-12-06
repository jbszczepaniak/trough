from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)


class Amount(models.Model):
    GRAM = 0
    PIECES = 1

    UNITS_CHOICES = (
        (GRAM, 'Gram'),
        (PIECES, 'Pieces'),
    )
    value = models.IntegerField(null=True)
    units = models.IntegerField(null=True   , choices=UNITS_CHOICES, default=GRAM)

class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)

class Ingredient(models.Model):
    name = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'name: {self.name}, ' \
               f'amount: {self.amount.value} {self.amount.get_units_display()}, ' \
               f'product: {self.product.name}'



