from django.contrib import admin
from .models import Meal, Drink, Side, Topping

# Register your models here.
admin.site.register(Meal)
admin.site.register(Drink)
admin.site.register(Side)
admin.site.register(Topping)
