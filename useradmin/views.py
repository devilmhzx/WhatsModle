import io
import os
import string
from datetime import timedelta

import random

from PIL import Image, ImageDraw, ImageFont
from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


from WhatsModle.settings import BASE_DIR
from useradmin.models import *


def register(request):
    JsonData = {'returnJson': '注册失败', 'states': ['已退出', '已登陆']}
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname', None)
        upwd = request.POST.get('upwd', None)
        vcode = request.POST.get('vcode', None)
        # 获取注册时上传的头像文件
        uicon = request.FILES.get('uicon',None)
        print(uname, upwd, vcode)
        # 校验验证码
        sessVcode = request.session.get('vcode', None)

        if uname and uicon and upwd and vcode and sessVcode and vcode.lower() == sessVcode.lower():
            user = UserRegister()
            user.uname = uname
            user.upwd = upwd
            user.uicon = uicon
            user.save()
            JsonData['returnJson'] = '注册成功'
        else:
            JsonData['returnJson'] = '注册失败'
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


# 生成并返回验证码
def getvcode(request):
    # 绘制验证码
    randomfont = random.sample(string.ascii_letters + string.digits, 4)
    vcode = ''.join(randomfont)
    # 保存该用户的验证码
    request.session['vcode'] = vcode
    # 创建画布
    # cr = random.randint(0, 255)
    # cg = random.randint(0, 255)
    # cb = random.randint(0, 255)

    image = Image.new('RGB', (200, 75), color=getChangeColor())
    # 创建画布的画笔
    draw = ImageDraw.Draw(image)
    # 绘制文字
    fontpath = os.path.join(BASE_DIR, 'static', 'font', 'A-OTF.otf')
    ifont = ImageFont.truetype(font=fontpath, size=40)
    # tr = random.randint(0, 255)
    # tg = random.randint(0, 255)
    # tb = random.randint(0, 255)
    randx = random.randint(40, 50)
    # randy = random.randint(20,50)
    for i in range(len(vcode)):
        draw.text((20 + randx * i, random.randint(10, 35)), vcode[i], fill=getChangeColor(), font=ifont)

    # 添加噪点
    for i in range(800):
        draw.point(getRangeInt(200, 75), getChangeColor())
    # 返回验证码
    # 创建字节容器
    buffer = io.BytesIO()
    # 将画布内容放入容器
    image.save(buffer, 'png')
    # 返回容器中的字节
    return HttpResponse(buffer.getvalue(), 'image/png')


def getRangeInt(x, y):
    randx = random.randint(0, x)
    randy = random.randint(0, y)
    return (randx, randy)


def getChangeColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)
