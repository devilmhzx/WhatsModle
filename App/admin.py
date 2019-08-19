from django.contrib import admin

# Register your models here.
from App.models import *


# 买家信息管理类
class BuyerAdmin(admin.ModelAdmin):
    # # 姓名
    # bname = models.CharField(max_length=20)
    # # 性别
    # bgender = models.NullBooleanField(default=None)
    # # 年龄
    # bage = models.IntegerField(default=18)
    # # 省份
    # bare = models.CharField(max_length=10)
    # # 职业
    # bjob = models.CharField(max_length=20)
    # bgender性别修改为中文

    def Gender(self):
        if self.bgender == None:
            return '不详'
        elif self.bgender:
            return '男'
        else:
            return '女'

    Gender.short_description = '性别'

    # 显示内容
    list_display = ['bname', Gender, 'bage', 'bare', 'bjob']
    # 搜索
    search_fields = ['bname', 'bjob']
    # 过滤
    list_filter = ['bgender', 'bare', 'bage', 'bjob']


# 账户信息管理类
class AccountAdmin(admin.ModelAdmin):
    # # 余额
    # amoney = models.FloatField(default=100)
    # # 账户
    # ano = models.CharField(max_length=20)
    # # 密码
    # apwd = models.CharField(max_length=20)
    # # 级别
    # atype = models.CharField(max_length=10, default='普通用户')
    list_display = ['ano', 'abuyer', 'amoney', 'atype']


# 订单信息管理类
class OrderAdmin(admin.ModelAdmin):
    # # 购买日期
    # odatetime = models.DateTimeField(auto_now_add=True)
    # # 购买金额
    # omoney = models.FloatField(default=0)
    # # 订单信息
    # oinfo = models.TextField(default='暂无内容')
    # # 订单状态
    # ostatus = models.IntegerField(default=0)
    list_display = ['odatetime', 'omoney', 'ostatus', 'oinfo']


# 商品信息管理类
class GoodsAdmin(admin.ModelAdmin):
    # # 名称
    # gname = models.CharField(max_length=20)
    # # 价格
    # gprice = models.FloatField(default=0)
    # # 详情
    # ginfo = models.TextField(default='暂无内容')
    # #商品类型
    # gType = models.CharField(max_length=10,default='未指定')
    list_display = ['gname', 'gprice', 'ginfo', 'gType']


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Goods, GoodsAdmin)
