from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def getarg(request, name, age, xingbie):
    return HttpResponse('获取的资料为：姓名：{}，年龄：{},性别：{}'.format(name, age, xingbie))


def getKwargs(request, name, age, xingbie):
    return HttpResponse('获取的资料为：姓名：%s，年龄：%s,性别：%s' % (name, age, xingbie))


def index(request):
    return render(request, 'links.html')
