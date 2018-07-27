from django.conf.urls import url
from books import views
from books.views import PublisherList


urlpatterns = [
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^publishers/$', PublisherList.as_view()),
]