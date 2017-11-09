from django.contrib import admin
from .models import ticket, order, side

# Register your models here.
admin.site.register(ticket)
admin.site.register(order)
admin.site.register(side)