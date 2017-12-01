from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [
    url(r'^register_user/$', views.register_user, name="register_user"),
]
