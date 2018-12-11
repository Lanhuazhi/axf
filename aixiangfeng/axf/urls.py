from django.conf.urls import url
from axf import views


urlpatterns = [
    #主页面
    url(r'^$',views.home,name='home'),

    #闪购商城页面
    url(r'^market/(\d+)/(\d+)/(\d+)/$',views.market,name='market'),

    #购物车页面
    url(r'^cart/$',views.cart,name='cart'),

    #我的页面
    url(r'^mine/$',views.mine,name='mine'),

    #登陆
    url(r'^login/$',views.Login,name='login'),

    #返回
    url(r'^return/',views.Return,name="return_back"),

    #获取短信验证码
    url(r'^send/$',views.Send,name='send'),

    #退出登陆
    url(r'^logout/',views.Loginout,name="logout"),

    #添加商品到购物车
    url(r'^addgoods/$',views.Addgooods,name="addgoods"),

    #删除不想要的商品
    url(r'^subgoods/$',views.SubShopping,name="subgoods"),

    #是否选择商品下单
    url(r'^isselect/$',views.Isselect,name="isselect"),

    #是否全选
    url(r'^allselect/$',views.Allselect,name="allselect"),

    #确认下单
    url(r'^comfirmorder/$',views.Comfirmorder,name="comfirmorder")
    #url(r'^market/(\d+)/',views.Market1,name='market1')
]