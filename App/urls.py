from django.contrib import admin
from django.urls import path, include

from App import views

urlpatterns = [
    path('addgoos', views.addGoos),
    path('delgoos', views.delGoos),
    path('modgoos', views.modGoos),
    path('getgoos', views.getGoos),
]