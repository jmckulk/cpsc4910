from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [
    url(r'^create_account/$', views.create_account, name="create_account"),
]