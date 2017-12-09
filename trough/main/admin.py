from django.contrib import admin

from trough.main.models import Ingredient, Product, Dish, Amount


class IngredientInline(admin.TabularInline):
    model = Ingredient


class DishAdmin(admin.ModelAdmin):
    model = Dish
    inlines = [IngredientInline]


admin.site.register(Dish, DishAdmin)

admin.site.register([Ingredient, Product, Amount])
