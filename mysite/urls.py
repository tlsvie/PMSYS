from django.conf.urls import url
from mysite import views


urlpatterns = [
    url(r'^about/$', views.about),
    url(r'^list/(?P<list_date>\d{4}/\d{1,2}/\d{1,2})$', views.listing),
    url(r'^$', views.index),
]