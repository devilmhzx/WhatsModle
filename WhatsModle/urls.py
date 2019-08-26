"""WhatsModle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # 将所有duoermei/开头的路由全部交给App下的urls.py去分发
    path('duoermei/', include('App.urls')),
    # 指定新模块
    # python3 Django 环境下，如果你遇到在根目录下urls.py中的include方法的第二个参数namespace添加之后就出错的问题。请在[app_name]目录下的urls.py中的urlpatterns前面加上app_name='[app_name]'， [app_name]代表你的应用的名称。
    # 例如：app_name ='[blog]' 
    #  ————————————————
    # 版权声明：本文为CSDN博主「他说少年如歌」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https://blog.csdn.net/qq_27437781/article/details/80436799
    path('news/', include('news.urls', namespace='newsns')),
    # 用户管理系统
    path('useradmin/', include('useradmin.urls', namespace='useradmin')),
]
