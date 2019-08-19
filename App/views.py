import time

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from App.models import *


def index(request):
    return HttpResponse('这是一个APP测试！')


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
