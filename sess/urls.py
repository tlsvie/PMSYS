from django.conf.urls import url
from sess import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login', views.login),
]