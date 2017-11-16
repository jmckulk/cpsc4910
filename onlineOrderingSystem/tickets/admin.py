from django.contrib import admin
from .models import Ticket, Meal, Side, Addition, Subtraction

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Meal)
admin.site.register(Side)
admin.site.register(Addition)
admin.site.register(Subtraction)
