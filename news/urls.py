from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

app_name = '[newsns]'
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^get/(\S+)/(\S+)/(\S+)', views.getarg, name='getstr'),
    url(r'^getkwargs/(?P<name>\S+)/(?P<xingbie>\S+)/(?P<age>\S+)', views.getKwargs, name='getKwargs'),
]
