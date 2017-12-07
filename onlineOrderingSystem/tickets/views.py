from django.shortcuts import render
from .models import Ticket, Side, Meal, Addition, Subtraction
from django.http import HttpResponseRedirect
from django.urls import reverse


# kitchen_view: renders the page for the kitchen to view while preparing orders
def kitchen_view(request):
    if request.user.is_authenticated:
        sixOldestTickets = Ticket.objects.order_by('creation_time_and_date')

        meals = {}
        sides = {}
        mealAdditions = {}
        mealSubtractions = {}
        sideAdditions = {}
        sideSubtractions = {}

        try:
            ticket1 = sixOldestTickets[0]
            if ticket1.fulfilled:
                ticket1 = None
            else:
                meals[ticket1.id] = Meal.objects.filter(ticket=ticket1)
                sides[ticket1.id] = Side.objects.filter(ticket=ticket1)

                mealAdditions[ticket1.id] = {}
                mealSubtractions[ticket1.id] = {}
                sideAdditions[ticket1.id] = {}
                sideSubtractions[ticket1.id] = {}

                for meal in meals[ticket1.id]:
                    mealAdditions[ticket1.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket1.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket1.id]:
                    sideAdditions[ticket1.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket1.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            print("ticket1 exception")
            ticket1 = None

        try:
            ticket2 = sixOldestTickets[1]
            if ticket2.fulfilled:
                ticket2 = None
            else:
                meals[ticket2.id] = Meal.objects.filter(ticket=ticket2)
                sides[ticket2.id] = Side.objects.filter(ticket=ticket2)

                mealAdditions[ticket2.id] = {}
                mealSubtractions[ticket2.id] = {}
                sideAdditions[ticket2.id] = {}
                sideSubtractions[ticket2.id] = {}

                for meal in meals[ticket2.id]:
                    mealAdditions[ticket2.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket2.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket2.id]:
                    sideAdditions[ticket2.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket2.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            ticket2 = None

        try:
            ticket3 = sixOldestTickets[2]
            if ticket3.fulfilled:
                ticket3 = None
            else:
                meals[ticket3.id] = Meal.objects.filter(ticket=ticket3)
                sides[ticket3.id] = Side.objects.filter(ticket=ticket3)

                mealAdditions[ticket3.id] = {}
                mealSubtractions[ticket3.id] = {}
                sideAdditions[ticket3.id] = {}
                sideSubtractions[ticket3.id] = {}

                for meal in meals[ticket3.id]:
                    mealAdditions[ticket3.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket3.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket3.id]:
                    sideAdditions[ticket3.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket3.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            ticket3 = None

        try:
            ticket4 = sixOldestTickets[3]
            if ticket4.fulfilled:
                ticket4 = None
            else:
                meals[ticket4.id] = Meal.objects.filter(ticket=ticket4)
                sides[ticket4.id] = Side.objects.filter(ticket=ticket4)

                mealAdditions[ticket4.id] = {}
                mealSubtractions[ticket4.id] = {}
                sideAdditions[ticket4.id] = {}
                sideSubtractions[ticket4.id] = {}

                for meal in meals[ticket4.id]:
                    mealAdditions[ticket4.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket4.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket4.id]:
                    sideAdditions[ticket4.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket4.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            ticket4 = None

        try:
            ticket5 = sixOldestTickets[4]
            if ticket5.fulfilled:
                ticket5 = None
            else:
                meals[ticket5.id] = Meal.objects.filter(ticket=ticket5)
                sides[ticket5.id] = Side.objects.filter(ticket=ticket5)

                mealAdditions[ticket5.id] = {}
                mealSubtractions[ticket5.id] = {}
                sideAdditions[ticket5.id] = {}
                sideSubtractions[ticket5.id] = {}

                for meal in meals[ticket5.id]:
                    mealAdditions[ticket5.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket5.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket5.id]:
                    sideAdditions[ticket5.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket5.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            ticket5 = None

        try:
            ticket6 = sixOldestTickets[5]
            if ticket6.fulfilled:
                ticket6 = None
            else:
                meals[ticket6.id] = Meal.objects.filter(ticket=ticket6)
                sides[ticket6.id] = Side.objects.filter(ticket=ticket6)

                mealAdditions[ticket6.id] = {}
                mealSubtractions[ticket6.id] = {}
                sideAdditions[ticket6.id] = {}
                sideSubtractions[ticket6.id] = {}

                for meal in meals[ticket6.id]:
                    mealAdditions[ticket6.id][meal.id] = Addition.objects.filter(meal=meal)
                    mealSubtractions[ticket6.id][meal.id] = Subtraction.objects.filter(meal=meal)

                for side in sides[ticket6.id]:
                    sideAdditions[ticket6.id][side.id] = Addition.objects.filter(side=side)
                    sideSubtractions[ticket6.id][side.id] = Subtraction.objects.filter(side=side)
        except:
            ticket6 = None

        is_manager = False
        if request.user.groups.filter(name='Manager').exists():
            is_manager = True

        return render(request, 'tickets/view_orders.html', {
            'ticket1': ticket1,
            'ticket2': ticket2,
            'ticket3': ticket3,
            'ticket4': ticket4,
            'ticket5': ticket5,
            'ticket6': ticket6,
            'meals': meals,
            'sides': sides,
            'mealAdditions': mealAdditions,
            'mealSubtractions': mealSubtractions,
            'sideAdditions': sideAdditions,
            'sideSubtractions': sideSubtractions,
            'is_manager': is_manager,
        })

    else:
        return HttpResponseRedirect(reverse('login:login'))


def fulfill_ticket(request, ticketID):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(id=ticketID)

        ticket.fulfilled = True
        ticket.save()

        return HttpResponseRedirect(reverse('tickets:kitchen_view'))

    else:
        return HttpResponseRedirect(reverse('login:login'))


def manager_view(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Manager'):
        all_tickets = Ticket.objects.order_by('creation_time_and_date')
        return render(request, 'tickets/tickets.html', {
            'alltickets': all_tickets
        })

    else:
        return HttpResponseRedirect(reverse('login:login'))
