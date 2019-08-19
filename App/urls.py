from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from App import views

urlpatterns = [
    path('addgoos', views.addGoos),
    path('delgoos', views.delGoos),
    path('modgoos', views.modGoos),
    path('getgoos', views.getGoos),

    # '''
    # 出处
    # https://blog.csdn.net/qq_42780289/article/details/95460043
    # 报错 " invalid escape sequence ‘\d’ " (无效的转义字符’\d’)。
    # 原因是Python 3将字符串文字解释为Unicode字符串，因此 \d 被视为转义的Unicode字符。解决办法有两种。
    # 方法1:
    # 在字符串字面值中使用两个反斜线， 表示正则表达式受到保护，不被字节码编译器解释。即把 \ 都变成 \\ 。
    # '''
    # path('getbuyeraccount/(\\d+)', views.GetBuyerAccount),
    # path('getaccountbuyer/(\\d+)', views.GetAccountBuyer),
    url(r'^getbuyeraccount/(\d+)', views.GetBuyerAccount),
    url(r'^getaccountbuyer/(\d+)', views.GetAccountBuyer),
    # buy/买家ID/商品ID
    url(r'^buy/(\d+)/(\d+)', views.Buy),
    # 查看买家购买的全部商品：路由的最后一段代表买家ID
    url(r'^getbuyergoods/(\d+)', views.GetBuyerGoods),
    # 查看商品的全部买家：理由最后一段代表商品的ID
    url(r'^getgoodsbuyer/(\d+)', views.GetGoodsBuyer),
]
