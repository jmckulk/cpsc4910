from django.db import models

# meal: contains info about a single meal on the menu
class meal(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)


# drink: contains info about a drink on the menu
class drink(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)


# side: contains info about side items on the menu
class side(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(default=0.0, null=False, blank=False)