import time

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from App.models import *


def index(request):
    return HttpResponse('这是一个APP测试！')


def addGoos(request):
    g = Goods()
    g.gname = '商品'+str(int(time.time()))

    g.save()
    return HttpResponse('OK')


def delGoos(request):
    return HttpResponse('OK')


def modGoos(request):
    return HttpResponse('OK')


def getGoos(request):
    return HttpResponse('OK')