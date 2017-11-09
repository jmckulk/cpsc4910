from django.db import models
from menu.models import meal, drink, side

# ticket: contains all top level info for a customer order ticket (customer info, pricing, etc)
class ticket(models.Model):
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_address = models.CharField(max_length=150, null=False, blank=False)
    customer_email_address = models.EmailField(max_length=100, null=False, blank=False)
    customer_phone_number = models.IntegerField(null=False, blank=False)

    price_pretax_total = models.IntegerField(null=False, blank=False)
    price_tax = models.IntegerField(null=False, blank=False)
    price_posttax_total = models.IntegerField(null=False, blank=False)

    creation_time_and_date = models.DateTimeField(auto_now=True, null=False, blank=False)

# order: contains info for single order item as well as ticket it is associated with
class order(models.Model):
    ticket = models.ForeignKey(ticket, models.CASCADE, null=False, blank=False)

    meal = models.ForeignKey(meal, models.SET_NULL, null=True, blank=True)
    drink = models.ForeignKey(drink, models.SET_NULL, null=True, blank=True)

    size_choices = (
        ('SM', 'small'),
        ('MD', 'medium'),
        ('LG', 'large')
    )
    size = models.CharField(max_length=2, choices=size_choices, default='MD')

# side: contains a side item for the order it relates to
class side(models.Model):
    order = models.ForeignKey(order, models.CASCADE, null=False, blank=False)

    side = models.ForeignKey(side, models.SET_NULL, null=True, blank=False)