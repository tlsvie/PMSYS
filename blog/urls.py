from django.conf.urls import url
from blog import views
from django.conf.urls.static import static
from PMSYS import settings
blog = 'blog'

urlpatterns = [
    url('^hello/$', views.hello),
    url('^time/$', views.dtime),
    url('^titles/$', views.blog_title, name="blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_article),

]

