from django.http import JsonResponse
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
    return None


def logout(request):
    return None


def mine(request):
    return None
