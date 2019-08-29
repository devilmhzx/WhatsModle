from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from useradmin import views

app_name = '[useradmin]'
urlpatterns = [
    # 用户管理系统
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mine/', views.mine, name='mine'),
    # 使用url配合正则来随即生成链接
    url(r'^getcode', views.getvcode, name='getcode')
]
