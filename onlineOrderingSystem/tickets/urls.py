from django.conf.urls import url
from . import views

app_name = 'tickets'

urlpatterns = [
    url(r'^kitchen_view/$', views.kitchen_view, name="kitchen_view"),
    url(r'^fulfill_ticket/(?P<ticketID>[0-9]+)/$', views.fulfill_ticket, name="fulfill_ticket"),
    url(r'^managertickets/$', views.manager_view, name="manager_view"),
]
