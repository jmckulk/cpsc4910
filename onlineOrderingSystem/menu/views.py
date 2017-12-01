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
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def remove_drink_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # for key in request.POST:
            #     print(key)
            for item, value in request.POST.items():
                try:
                    object = Drink.objects.get(id=item)
                    if object is not "":
                        object.current_drink_item = False
                        object.save()
                except ValueError:
                    pass
            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def remove_side_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # for key in request.POST:
            #     print(key)
            for item, value in request.POST.items():
                try:
                    object = Side.objects.get(id=item)
                    if object is not "":
                        object.current_side_item = False
                        object.save()
                except ValueError:
                    pass
            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def remove_menu_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # for key in request.POST:
            #     print(key)
            for item, value in request.POST.items():
                try:
                    object = Meal.objects.get(id=item)
                    if object is not "":
                        object.current_menu_item = False
                        object.save()
                except ValueError:
                    pass
            return HttpResponseRedirect(reverse('menu:menu'))

        else:
            return HttpResponseRedirect(reverse('login:index'))

    else:
        return HttpResponseRedirect(reverse('login:login'))
