from django.conf.urls import url
from . import views

app_name = 'menu'

urlpatterns = [
    # api access points for dealing with questionnaire data
    url(r'^menu/$', views.menu, name="menu"),
]
