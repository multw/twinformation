"""testdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dbconn import views

urlpatterns = [
	url(r'^$', views.homepage), # "^"符號表示字串開頭，"$"表示字串結尾
	url(r'^post/(\w+)$', views.showpost),
    url(r'^currency/(?P<currency>[A-Z]{3})/$', views.USD),
    url(r'^oilprice/$', views.Oilprice),
    url(r'^rate/$', views.Rate),
    url(r'^invoice/$', views.Invoice),
    url(r'^admin/',  include(admin.site.urls)),
]
