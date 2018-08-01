from django.conf.urls import url
from sess import views


urlpatterns = [
    url(r'^$', views.login),
]