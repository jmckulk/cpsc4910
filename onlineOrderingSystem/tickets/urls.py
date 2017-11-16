from django.conf.urls import url
from . import views

app_name = 'tickets'

urlpatterns = [
    # api access points for dealing with questionnaire data
    url(r'^kitchen_view/$', views.kitchen_view, name="kitchen_view"),
]