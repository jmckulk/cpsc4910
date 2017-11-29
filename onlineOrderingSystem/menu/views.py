from django.shortcuts import render
from .models import Meal, Side, Drink
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def menu(request):
    if request.user.is_authenticated:
        all_menu_items = Meal.objects.order_by('id')
        all_side_items = Side.objects.order_by('id')
        all_drink_items = Drink.objects.order_by('id')
        return render(request, 'menu/menu.html', {
            'allmenuitems': all_menu_items,
            'allsideitems': all_side_items,
            'alldrinkitems': all_drink_items,
        })

    else:
        return HttpResponseRedirect(reverse('login:login'))

# def manager_view(request):
#     if request.user.is_authenticated:
#         all_tickets = Ticket.objects.order_by('creation_time_and_date')
#         return render(request, 'tickets/tickets.html', {
#             'alltickets': all_tickets
#         })
#
#     else:
#         return HttpResponseRedirect(reverse('login:login'))
