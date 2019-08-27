from datetime import timedelta

from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from useradmin.models import *


def register(request):
    JsonData = {'returnJson': '注册失败', 'states': ['已退出', '已登陆']}
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname', None)
        upwd = request.POST.get('upwd', None)
        print(uname, upwd)

        if uname and upwd:
            user = UserRegister()
            user.uname = uname
            user.upwd = upwd
            user.save()
            JsonData['returnJson'] = '注册成功'
        else:
            pass
        ReturnJson = JsonResponse(JsonData['returnJson'], safe=False)
        return ReturnJson


def login(request):
    JsonData = {'returnJson': '登录失败', 'states': ['已退出', '已登陆']}
    httpRe = HttpResponse()
    if request.method == 'GET':
        return render(request, 'Login.html')
    else:
        uname = request.POST.get('uname', None)
        upwd = request.POST.get('upwd', None)

        user = UserRegister.objects.filter(uname=uname).first()
        if user and upwd == user.upwd:
            JsonData['returnJson'] = '登录成功'
            JsonData['states'] = '已登录'
            # 通过客户端(cookie)保存用户状态
            # httpRe.set_cookie('uname', uname, max_age=60)
            httpRe.set_cookie('uname', uname, expires=timedelta(days=1))
            # 让服务端通过session来保存用户状态

        httpRe.content = JsonData.items()
        # ReturnJson = JsonResponse(JsonData)

        return httpRe


def logout(request):
    httpRe = HttpResponse()
    # 让客户端删除保存的用户状态
    httpRe.delete_cookie('uname')
    # 删除服务端session

    httpRe.content = '登出成功'
    return httpRe


def mine(request):
    # 从COOKIE中获取用户状态
    uname = request.COOKIES.get('uname', None)
    # 从服务端session获取用户状态

    uname = uname if uname != None else '你还未登录'
    return HttpResponse('你好，' + uname)
