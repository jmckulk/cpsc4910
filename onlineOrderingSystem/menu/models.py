from django.db import models


# Drink: contains info about a drink on the menu
class Drink(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)
    current_menu_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Side: contains info about side items on the menu
class Side(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)
    current_menu_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Topping: contains info about topping for menu items
class Topping(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)
    current_menu_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Meal: contains info about a single meal on the menu
class Meal(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    side = models.ForeignKey(Side, models.SET_NULL, null=True, blank=True)
    has_drink = models.BooleanField(default=False)
    price = models.FloatField(default=0.0, null=False, blank=False)
    current_menu_item = models.BooleanField(default=True)

    def __str__(self):
        return self.name
