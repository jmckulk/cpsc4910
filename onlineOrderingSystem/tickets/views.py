from django.shortcuts import render
from .models import Ticket, Side, Meal

# Create your views here.
def kitchen_view(request):
    sixOldestTickets = ticket.objects.order_by('creation_time_and_date')

    return render(request, 'tickets/view_orders.html', {
        'displayTickets': sixOldestTickets,
    })