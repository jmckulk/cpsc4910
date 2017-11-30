from django.conf.urls import url
from . import views

app_name = 'menu'

urlpatterns = [
    url(r'^menu/$', views.menu, name="menu"),
    url(r'^create_meal/$', views.create_meal, name="create_meal"),
    url(r'create_side/$', views.create_side, name="create_side"),
    url(r'create_drink/$', views.create_drink, name="create_drink"),
]
