from django.conf.urls import url
from account import views
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
account = 'account'

urlpatterns = [
    url('^login/$', views.user_login, name="user_login"),
    #url('^login/$', auth_views.login, name="user_login"),

]

