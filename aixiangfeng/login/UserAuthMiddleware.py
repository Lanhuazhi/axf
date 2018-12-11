from django.http import  HttpResponseRedirect
from django.shortcuts import redirect


#Django 没有MiddlewareMixin这个类需要定义一个这样的类，因为自定义中间件需要继承这个类
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Login(MiddlewareMixin):

    def process_request(self,request):
        # 点击的是登录页面则正常执行
        # if request.path == '/login/':
        #     print("*********进去了吗")
        #     return None
        #验证点击该页面是是否已经登录
        # 点击的是cart或者是mine页面
        if request.path == '/cart/' or request.path == '/mine/':
            #是否登陆
            user_sessions = request.session.get("isLogin")
            #print(user_sessions)
            if user_sessions:
                #登陆了则返回none
                return None
           #没登陆则返回登陆界面让用户登陆
            return redirect('axf:login')
