from django.db import models


# Create your models here.
# 买家信息
class Buyer(models.Model):
    # 姓名
    bname = models.CharField(max_length=20)
    # 性别
    bgender = models.NullBooleanField(default=None)
    # 年龄
    bage = models.IntegerField(default=18)
    # 省份
    bare = models.CharField(max_length=10)
    # 职业
    bjob = models.CharField(max_length=20)

    def __str__(self):
        return self.bname


# 账户信息
class Account(models.Model):
    # 账户
    ano = models.CharField(max_length=20,unique=True)
    # 余额
    amoney = models.FloatField(default=100)
    # 密码
    apwd = models.CharField(max_length=20,default='111111')
    # 级别
    atype = models.CharField(max_length=10, default='普通用户')
    # 买家-账户（一对一关系）
    abuyer = models.OneToOneField(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.ano



# 订单信息
class Order(models.Model):
    # 购买日期
    odatetime = models.DateTimeField(auto_now_add=True)
    # 购买金额
    omoney = models.FloatField(default=0)
    # 订单信息
    oinfo = models.TextField(default='暂无内容')
    # 订单状态
    ostatus = models.IntegerField(default=0)

    # 订单所属买家(一对多)
    obuyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order{otime=' + str(self.odatetime) + ',omoney=' + str(self.omoney) + ',ostatus=' + str(
            self.ostatus) + ',oinfo=' + self.oinfo + '}'


# 商品信息
class Goods(models.Model):
    # 名称
    gname = models.CharField(max_length=20,unique=True)
    # 价格
    gprice = models.FloatField(default=0)
    # 详情
    ginfo = models.TextField(default='暂无内容')
    # 商品类型
    gType = models.CharField(max_length=10, default='未指定')

    # 购买该商品的买家们（多对多）
    gbuyers = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.gname
