"""PMSYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from mainsite import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url('account/', include(('account.urls', 'account'), namespace='account')),
    url('books/', include('books.urls')),
    url('mysite/', include('mysite.urls')),
    url('^$', views.homepage),
    url(r'^post/(\w+)$', views.showpost),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^sess/', include('sess.urls')),


]
