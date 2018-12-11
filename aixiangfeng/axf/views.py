from django.shortcuts import render,redirect
from .models import Wheel,Nav,Shop,Mainshow,Market,Goods,Cartgoods,Oder
import zhenzismsclient as smsclient
from django.http import JsonResponse
import random
import time
from django.contrib.auth import logout


# Create your views here.


#首页页面
def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    #必购部分，下架了
    #mustbuyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    #商品信息展示
    mainshow = Mainshow.objects.all()
    return render(request,
                  'home.html',
                  {'wheelsList':wheelsList,
                   'navList':navList,
                   'shop1':shop1,
                   'shop2':shop2,
                   'mainshow':mainshow
                   })


#闪送超市页面
def market(request,typeid,cid,sortid):
    foodtypes = Market.objects.all()
    if cid == '0':
        #全部分类
        goods = Goods.objects.filter(categoryid=typeid)
    else:
        #子分类标签商品的展示
        goods = Goods.objects.filter(categoryid=typeid,childcid=cid)

    #排序
    #销量排序
    if sortid =='1':
        goods = goods.order_by('productnum')
    #价格降序
    elif sortid =='2':
        goods = goods.order_by('-price',)
    #价格升序
    elif sortid =='3':
        goods = goods.order_by('price')

    #全部分类里的子分类标签展示
    group = foodtypes.get(typeid = typeid)
    childtypename = group.childtypenames
    childtypenameList = []
    Lst = childtypename.split('#')
    for lst in Lst:
        Lst1 = lst.split(':')
        data ={
            'Childname':Lst1[0],
            'Childid':Lst1[1]
        }
        childtypenameList.append(data)

    #判断用户登陆后是否有添加商品，有就展示在界面
    userphone = request.session.get("userphone")
    usergoodList = []
    if userphone:
        usergood = Cartgoods.objects.filter(userid=userphone)
        usergoodList = usergood.all()

    for good in goods:
        for item in usergoodList:
            if item.productid == good.productid:
                good.number = item.goodsnumber

    return render(request,'market.html',{'foodtypes':foodtypes,
                                         'goods':goods,
                                         'childtypeList':childtypenameList,
                                         'typeid':typeid,
                                         'cid':cid,
                                         })


#添加商品到购物车
#增加商品
def Addgooods(request):
    #判断用户是否已经登陆
    prices=0
    userphone = request.session.get("userphone")
    #没登陆
    if not userphone:
        #让用户登陆
        return JsonResponse({"status":901})
    goodsid = request.POST.get("goodsid")
    print(goodsid)
    usergoods = Goods.objects.get(productid=goodsid)
    print(usergoods.productid)
    #判断是否商品库存量是否足够
    if usergoods.storenums == '0':
        return JsonResponse({"msg":"库存不足，正在努力补货中...","status":"error"})

        #判断用户是否有订单

    try:
        usergood = Cartgoods.objects.filter(userid=userphone)
        usergood = usergood.get(productid=goodsid)
        if usergood:
            usergood.goodsnumber += 1
            usergoods.storenums = int(usergoods.storenums) - 1
            usergood.price = (usergoods.price)*(usergood.goodsnumber)
            usergood.save()
            usergoods.save()
            prices = goodsprices(userphone)

    except Cartgoods.DoesNotExist:
        usergood = Cartgoods(userid=userphone,productid=goodsid,
                                goodsnumber=1,price=usergoods.price,
                                is_select=True,productimg=usergoods.productimg,
                                productname=usergoods.productlongname,
                                isDelete=False
                                )
        usergood.save()
    return JsonResponse({"data":usergood.goodsnumber,"status":200,"msg":usergood.price,"prices":prices})
    # #判断该商品是否添加


#删除商品
def SubShopping(request):
    prices=0
    userphone = request.session.get("userphone")
    if not userphone:
        return JsonResponse({"status":901})
    goodsid = request.POST.get("goodsid")
    usergoods = Goods.objects.get(productid=goodsid)
    print(usergoods.productid)

    try:
        usergood = Cartgoods.objects.filter(userid=userphone)

    except Cartgoods.DoesNotExist:

        usergood = None

    if usergood:
        usergood = usergood.get(productid=goodsid)
        usergood.goodsnumber -= 1
        usergoods.storenums = int(usergoods.storenums) + 1
        usergood.price -= usergoods.price
        if usergood.goodsnumber ==0:
            usergood.delete() #当用户减到0时从数据库删除该条商品数据
        else:
            usergood.save()
            usergoods.save()
            prices = goodsprices(userphone)

    return JsonResponse({"data":usergood.goodsnumber,"status":200,"msg":usergood.price,"prices":prices})


#是否选择商品,单选
def Isselect(request):
    prices = 0
    userphone = request.session.get("userphone")
    groupimg = request.POST.get("groupimg")
    group =Cartgoods.objects.filter(userid=userphone)
    groupimg =group.get(productid=groupimg)
    if groupimg.is_select:
        groupimg.is_select = False
        groupimg.save()
        prices = goodsprices(userphone)
        return JsonResponse({'data':groupimg.is_select,"prices":prices})
    else:
        groupimg.is_select =True
        groupimg.save()
        prices = goodsprices(userphone)
        return JsonResponse({'data':groupimg.is_select,"prices":prices})


#是否全选
def Allselect(request):
    prices=0
    data = ""
    userphone = request.session.get("userphone")
    usergood = Cartgoods.objects.filter(userid=userphone)
    a = request.POST.get("a")
    for items in usergood:
        if a == "0":
            items.is_select = False
            items.save()
            prices = goodsprices(userphone)
            data = False
        else:
            items.is_select = True
            items.save()
            prices = goodsprices(userphone)
            data = True
    return JsonResponse({"data":data,"prices":prices})


#确认下单
def Comfirmorder(request):
    userphone = request.session.get("userphone")
    times = request.POST.get("times")
    #print(times)
    remarks = request.POST.get("remarks")
    #print(remarks)
    usergood = Cartgoods.objects.filter(userid=userphone,is_select=True)
    #print(usergood)
    if not usergood:
        return JsonResponse({"data":"erorr"})

    # #生成订单号
    else:
        orderid = int(time.strftime("%Y%m%d",time.localtime(time.time())))+random.randint(1000,9999)
        #print(orderid)
        ordergoods = Oder(times=times,remarks=remarks,ordid=orderid,userid=userphone)
        ordergoods.save()
        for item in usergood:
            item.isDelete = True
            item.orderid = orderid
            item.save()
        return JsonResponse({"data":"sucess"})




#第三平台榛子短信验证码的获取
def Send(request):
    phonenumber = request.POST.get("phones")
    print(phonenumber)
    #判断手机账号是否存在，不需要了，不设置注册项
    # try:
    #     userphones = User.objects.get(userphones=phonenumber)
    # except User.DoesNotExist:
    #     userphones = None
    # if userphones:
    #     return JsonResponse({"data": "手机账号已存在"})
    #随机生成一个验证码信息
    code = random.randint(1000, 9999)
    print(code)
    #将注册第三方平台的短信验证码的url\appid\appsecert传入
    client = smsclient.ZhenziSmsClient(
        "https://sms_developer.zhenzikj.com.",
        "100192",
        "cf470b40-1a12-4343-ba4d-e0bdad44dd26")

    #向用户手机发送验证码
    client.send(phonenumber,"欢迎使用爱鲜蜂，您的验证码是:"+str(code))
    print(client.send(phonenumber,"欢迎使用爱鲜蜂，您的验证码是:"+str(code)))
    #只能存一次，验证码每次登陆都会不一样，所以这个是不行的
    # user = User.objects.create_user(username=phonenumber,password=code)
    # user.save()
    #将验证码存入session中，以便后面验证
    request.session["code"] = code
    return JsonResponse({"data":"发送成功","code":code})


#登陆页面
def Login(request):
    if request.method == "POST":
        userphone = request.POST.get("phones")
        passwords = request.POST.get("code")
        print(passwords)
        code = request.session.get("code")
        if passwords == str(code):
            request.session["isLogin"] = True
            request.session["userphone"] = userphone
            return JsonResponse({"msg":"ok"})
        else:
            return JsonResponse({"msg": "验证码错误"})
    return render(request,'login.html')

#返回
def Return(request):
    return redirect("axf:home")


#退出登陆
def Loginout(request):
    logout(request)
    return redirect("axf:home")

#购物车页面
def cart(request):
    userphone = request.session.get("userphone")
    usergood = Cartgoods.objects.filter(userid=userphone)
    if usergood:
        prices =goodsprices(userphone)
        # for lst in usergood:
        #     prices += lst.price
        return render(request,'cart.html',{'usergood':usergood,"prices":prices})
    else:
        return render(request,'cart0.html')


#购物车商品总价的计算
def goodsprices(userphone):
    usergood = Cartgoods.objects.filter(userid=userphone)
    prices = 0
    for item in usergood:
        if item.is_select:
            prices += item.price
    return prices




#我的页面
def mine(request):
    usename = request.session.get("userphone")
    return render(request,'mine.html',{"username":usename})



