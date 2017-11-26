from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    #url(r'^login/$', views.login, name="login"),
	url(r'^login/$', auth_views.login, name='login'),
]