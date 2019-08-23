import time

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from App.models import *


def index(request):
    b = Buyer.objects.all()
    g = Goods.objects.all()

    DataDirc = {
        'Buyer': b,
        'Goods': g,
    }
    return render(request, 'index.html', context=DataDirc)


def addGoos(request):
    g = Goods()
    g.gname = '商品' + str(int(time.time()))
    g.ginfo = '此条是卖家通过路由创建的商品'
    g.save()
    return HttpResponse(g.gname + '创建成功！')


def delGoos(request):
    g = Goods.objects.last()  # 删除最后一个商品
    g.delete()
    return HttpResponse(g.gname + '删除成功!')


# 改
def modGoos(request):
    g = Goods.objects.last()
    g.ginfo = g.gname + '修改后的！'
    g.save()
    return HttpResponse(g.gname + '修改成功')


# 查
def getGoos(request):
    gs = Goods.objects.filter(gprice__gt=0)
    rt = ''
    for g in gs:
        rt += (g.gname + ';')
    return HttpResponse(rt)


# 通过Buyer获得账户信息
def GetBuyerAccount(request, BuyerId):
    b = Buyer.objects.get(pk=BuyerId)
    ba = b.account
    return HttpResponse(b.bname + '的账号是' + ba.ano)


# 通过账户获得买家信息
def GetAccountBuyer(request, AccountId):
    a = Account.objects.get(pk=AccountId)
    ab = a.abuyer
    return HttpResponse('账户' + a.ano + '的买家是：' + ab.bname)


def Buy(request, BuyerID, GoosID):
    # 向商品的gbuyers添加一个新的买家
    g = Goods.objects.get(pk=GoosID)
    b = Buyer.objects.get(pk=BuyerID)
    g.gbuyers.add(b)
    g.save()

    # 生成订单对象
    o = Order()
    o.omoney = g.gprice
    o.obuyer = b
    b.account.amoney -= o.omoney
    o.oinfo = b.bname + '购买了' + g.gname + ',花了' + str(g.gprice) + '元！' + '剩余款项为：' + str(b.account.amoney)
    b.save()
    o.save()
    return HttpResponse(b.bname + '成功购买了一件' + g.gname + '!' + o.oinfo)


def GetBuyerGoods(request, BuyerID):
    b = Buyer.objects.get(pk=BuyerID)
    gs = b.goods_set.all()
    rt = ''
    for g in gs:
        rt += g.gname + ';'
    return HttpResponse(b.bname + '购买了：' + rt)


def GetGoodsBuyer(request, GoodsID):
    g = Goods.objects.get(pk=GoodsID)
    bs = g.gbuyers.all()
    rt = ''
    for b in bs:
        rt += b.bname + ';'
    return HttpResponse(g.gname + '的买家有：' + rt)


def GetBuyerOrders(request, BuyerID):
    b = Buyer.objects.get(pk=BuyerID)
    os = b.order_set.all()
    rt = ''
    for i in os:
        rt += i.oinfo + ';\n'
    return HttpResponse(b.bname + '购买的订单为：' + rt)


