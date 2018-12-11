from django.db import models

# Create your models here.


#轮播图片管理
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

#必购部分，下架
# class Mustbuy(models.Model):
#     img = models.CharField(max_length=150)
#     name = models.CharField(max_length=20)
#     trackid = models.CharField(max_length=20)

#便利店
class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)


#首页展示页面
class Mainshow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=150)
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)


    img1 = models.CharField(max_length=150)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=25)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)


    img2 = models.CharField(max_length=150)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=25)
    price2 = models.CharField(max_length=10)
    marketprice2= models.CharField(max_length=10)


    img3 = models.CharField(max_length=150)
    childcid3 = models.CharField(max_length=20)
    productid3= models.CharField(max_length=20)
    longname3 = models.CharField(max_length=25)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

#闪购超市
class Market(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=10)
    childtypenames =  models.TextField(max_length=100)
    typesort = models.CharField(max_length=10)


#闪购超市的商品详细信息展示
class Goods(models.Model):
    productid = models.CharField(max_length=10) #商品id
    productimg = models.CharField(max_length=150) #商品图片
    productname = models.CharField(max_length=150) # 商品名称
    productlongname = models.CharField(max_length=150) # 商品详细名称
    isxf= models.CharField(max_length=10) # 是否为精选
    pmdesc = models.CharField(max_length=10)
    specifics = models.CharField(max_length=10) # 规格
    price = models.IntegerField()# 商品的折后价格
    marketprice = models.CharField(max_length=10) # 商品的原价
    categoryid = models.CharField(max_length=10) # 分类的id
    childcid = models.CharField(max_length=10)  # 子分类的id
    childcidname = models.CharField(max_length=50)  # 子分类的名称
    dealerid = models.CharField(max_length=10)
    storenums = models.CharField(max_length=10) #库存
    productnum = models.IntegerField()# 销量排序



#添加商品到购物车
#购物车表
class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDelete=False)


class Cartgoods(models.Model):
    userid = models.CharField(max_length=15)    #用户ID

    productid = models.CharField(max_length=11)   #商品id

    goodsnumber = models.IntegerField()   #数量

    price = models.IntegerField()     #总价

    is_select = models.BooleanField(default=True)     #是否选中

    productimg = models.CharField(max_length=150)     #商品图片

    productname = models.CharField(max_length=150)    #商品名称

    orderid = models.CharField(max_length=20,default=0) #订单id

    isDelete = models.BooleanField(default=False) #是否删除

    objects = Manager()


#生成订单
class Oder(models.Model):
    #配送时间
    times = models.CharField(max_length=50)

    #备注
    remarks = models.CharField(max_length=200)

    #订单号
    ordid = models.CharField(max_length=20)

    #用户id
    userid = models.CharField(max_length=15)



