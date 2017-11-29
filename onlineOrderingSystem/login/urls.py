from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^login/$', views.userLogin, name="login"),
    url(r'^logout/$', views.userLogout, name='logout'),
    url(r'^$', views.index, name='index'),
]