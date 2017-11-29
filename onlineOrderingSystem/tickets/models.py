from django.db import models
from menu.models import Meal as MenuMeal
from menu.models import Drink as MenuDrink
from menu.models import Side as MenuSide
from menu.models import Topping as MenuTopping
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Ticket: contains all top level info for a customer order ticket (customer info, pricing, etc)
class Ticket(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_address = models.CharField(max_length=150, null=False, blank=False)
    customer_email_address = models.EmailField(max_length=100, null=False, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    customer_phone_number = models.CharField(validators=[phone_regex], max_length=15, null=False, blank=False)

    price_pretax_total = models.FloatField(default=0.0, null=False, blank=False)
    price_tax = models.FloatField(default=0.0, null=False, blank=False)
    price_posttax_total = models.FloatField(default=0.0, null=False, blank=False)

    creation_time_and_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        if self.fulfilled:
            return "[FULFILLED] [" + str(self.creation_time_and_date) + "] " + self.customer_name
        else:
            return "[" + str(self.creation_time_and_date) + "] " + self.customer_name


# Meal: contains info for single meal item for a ticket
class Meal(models.Model):
    ticket = models.ForeignKey(Ticket, models.CASCADE, null=False, blank=False)

    meal = models.ForeignKey(MenuMeal, models.SET_NULL, null=True, blank=True)
    drink = models.ForeignKey(MenuDrink, models.SET_NULL, null=True, blank=True)

    size_choices = (
        ('SM', 'small'),
        ('MD', 'medium'),
        ('LG', 'large')
    )
    size = models.CharField(max_length=2, choices=size_choices, default='MD')

    def clean(self):
        if not (self.meal or self.drink):
            raise ValidationError("An Meal must have a meal item AND/OR a drink")

    def __str__(self):
        if self.meal is not None:
            return self.meal.name + "[ticket: " + str(self.ticket.id) + "]"
        elif self.drink is not None:
            return self.drink.name + "[ticket: " + str(self.ticket.id) + "]"
        else:
            return "{MENU ITEM NOT FOUND} [ticket: " + str(self.ticket.id) + "]"


# Side: contains a side item for the meal it relates to
class Side(models.Model):
    ticket = models.ForeignKey(Ticket, models.CASCADE, null=False, blank=False)

    side = models.ForeignKey(MenuSide, models.SET_NULL, null=True, blank=False)

    def __str__(self):
        if self.side is not None:
            return self.side.name + "[ticket: " + str(self.ticket.id) + "]"
        else:
            return "{SIDE ITEM NOT FOUND} [ticket: " + str(self.ticket.id) + "]"


# Addition: contains an addition to the current item
class Addition(models.Model):
    meal = models.ForeignKey(Meal, models.CASCADE, null=True, blank=True)
    side = models.ForeignKey(Side, models.CASCADE, null=True, blank=True)

    add = models.ForeignKey(MenuTopping, models.SET_NULL, null=True, blank=False)

    def clean(self):
        if not (self.meal or self.side):
            raise ValidationError("An Addition must be associated with an MenuMeal OR a MenuSide")

    def __str__(self):
        if self.add is not None:
            if self.meal is not None:
                return self.add.name + "[item: " + self.meal.meal.name + " | ticket: " + str(self.meal.ticket.id) + "]"
            else:
                return self.add.name + "[item: " + self.side.side.name + " | ticket: " + str(self.side.ticket.id) + "]"
        else:
            return "{ADDITION NOT FOUND} [ticket: ERROR]"


# Subtraction: contains a subtraction from the specified item
class Subtraction(models.Model):
    meal = models.ForeignKey(Meal, models.CASCADE, null=True, blank=True)
    side = models.ForeignKey(Side, models.CASCADE, null=True, blank=True)

    sub = models.ForeignKey(MenuTopping, models.SET_NULL, null=True, blank=False)

    def clean(self):
        if not (self.meal or self.side):
            raise ValidationError("A Subtraction must be associated with an MenuMeal OR a MenuSide")

    def __str__(self):
        if self.sub is not None:
            if self.meal is not None:
                return self.sub.name + "[item: " + self.meal.meal.name + " | ticket: " + str(self.meal.ticket.id) + "]"
            else:
                return self.sub.name + "[item: " + self.side.side.name + " | ticket: " + str(self.side.ticket.id) + "]"
        else:
            return "{SUBTRACTION NOT FOUND} [ticket: ERROR]"
