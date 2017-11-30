from django.shortcuts import render
from .models import Meal, Side, Drink
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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


def create_meal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mealName = request.POST.get("mealName", "")
            description = request.POST.get("description", "")
            sideID = request.POST.get("mealSide", "")
            price = request.POST.get("price", "")

            if "mealHasDrink" in request.POST:
                hasDrink = True
            else:
                hasDrink = False

            if mealName == "" or description == "" or price == "" or sideID == "":
                return HttpResponseRedirect(reverse('menu:menu'))

            meal = Meal()
            meal.name = mealName
            meal.description = description
            meal.side = Side.objects.get(id=sideID)
            meal.has_drink = hasDrink
            meal.current_menu_item = True
            meal.price = price

            meal.save()

            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def create_side(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sideName = request.POST.get("sideName", "")
            price = request.POST.get("sidePrice", "")

            if sideName == "" or price == "":
                return HttpResponseRedirect(reverse('menu:menu'))

            side = Side()
            side.name = sideName
            side.price = price
            side.current_menu_item = True

            side.save()

            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def create_drink(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            drinkName = request.POST.get("drinkName", "")
            price = request.POST.get("drinkPrice", "")

            if drinkName == "" or price == "":
                return HttpResponseRedirect(reverse('menu:menu'))

            drink = Drink()
            drink.name = drinkName
            drink.price = price
            drink.current_menu_item = True

            drink.save()

            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('menu:index'))

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
