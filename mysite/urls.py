from django.conf.urls import url
from mysite import views


urlpatterns = [
    url(r'^about/$', views.about),
    url(r'^list/(?P<list_date>\d{4}/\d{1,2}/\d{1,2})$', views.listing),
    url(r'^$', views.index),
    url(r'^detail/(\d+)$', views.detail,name="detail_url"),
    url(r'^myform/$', views.myform),
    url(r'^indexform/$', views.indexform),
    url(r'^contact/$', views.contact),
]