
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from book.models import BookInfo

# Create your views here.

"""
视图
1.就是python函数
2.函数的第一个参数就是  请求  和请求相关的
3.我们必须要返回一个响应  响应是HTTPResponse的实例对象/子类实例对象
"""


def index(request):
    # 实现业务逻辑
    # 1.先把所以书籍查询出来
    # sql实现 select * from bookinfo
    # ORM
    books = BookInfo.objects.all()
    # books = [BookInfo.objects.all()]
    context = {
        'books': books
    }
    
    # path = reverse('book:index')
    # return redirect(path)
    
    # render
    # 参数1：当前的请求
    # 参数2：模板文件
    # 参数3：context传递参数
    return render(request, 'index.html', context=context)
    
    # return HttpResponse('index')


def detail(request, catageory_id, book_id):
    # print(catageory_id, book_id)
    
    #########################查询字符串###########################
    """
    以? 作为分隔符
    ? 前面 表示 路由
    ? 后面 表示 get方式传递的参数 称之为 查询字符串
    ?key=value&key=value...
    """
    ################################GET #############################
    # # 获取传递的参数
    # query_params = request.GET
    # # query_params: QueryDict: {'username': ['xxx', 'yyy'], 'password': ['xxx']}
    # # QueryDict 以普通的字典形式来获取 一键多值的时候 只能获取最后的那一个值
    # # 想获取 一键多值的话 就需要使用 QueryDict 的getlist方法
    # username = query_params['username']
    # username = query_params.get('username')
    # username = query_params.getlist('username')
    
    #################################POST 表单数据##################################
    # data = request.POST
    
    #################################POST json数据##################################
    # # JSON 里面是双引号
    # body = request.body # byte类型
    # body_str = body.decode()    # JSON形式的字符串, python3.6 无需执行此步
    # body_dict = json.load(body_str)
    #############################请求头#######################################
    # print(request.META)
    # content_type = request.META['content_type']
    ################################HttpResponse###################################
    # HttpResponse
    # content 传递字符串 不要传递 对象，字典等数据
    # status 范围：100-599
    # content_type 是一个MIME类型
    #               语法形式是: 大类/小类
    #   text/html text/css text/javascript
    #   application/json
    #   image/png   ...
    return HttpResponse('detail', status=200, content_type='')
    ################################JsonResponse###################################
    from django.http import JsonResponse
    data = {'name': 'xxx'}
    return JsonResponse(data)
    
    #################################跳转页面###################################
    # 跳转到首页
    path = reverse('book:index')
    return redirect(path)
    return redirect('http://www.baidu.com')


"""
保存在客服端的数据叫 cookie
    cookie是基于域名(IP)的
    1.流程
    2.效果
    3.从http协议角度深入掌握cookie的流程(原理)
"""


def set_cookie(request):
    # 1.先判断有没有cookie信息
    # 假设没有
    # 2.获取用户名
    username = request.GET.get('username')
    # 3.因为我们假设没有cookie信息,我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')
    # key, value
    # max_age 单位是秒
    # 时间是 从服务器接受到这个请求时间 + 秒数 计算之后的时间
    response.set_cookie('username', username)  # 临时
    response.set_cookie('username', username, max_age=3600)  # 1小时
    
    # # 删除cookie的2中方式
    # response.set_cookie(key, value, max_age=0)
    # response.delete_cookie(key)
    
    # 4.返回相应
    return response


def get_cookie(request):
    """
    # 第二次及其之后的过程
    # 第二次及其之后的请求都会携带cookie信息
    
    :param request:
    :return:
    """
    # 1.服务器可以接收(查看)cookie信息
    cookies = request.COOKIES
    # cookies 就是一个字典
    username = cookies.get('username')
    # 2.得到用户信息就可以继续其他的业务逻辑了
    return HttpResponse('get_cookie')


"""
保存在服务器的数据叫 session
    session需要依赖于cookie
如果浏览器禁用了cookie, 则session不能实现
    0.概念
    1.流程
        第一次请求:
            ① 我们第一次请求的时候可以携带一些信息(用户名/密码) cookie中没有任何信息
            ② 当我们的服务器接受到这个请求之后,进行用户名和密码的验证,验证没有问题可以设置
                session信息
            ③ 在设置session信息的同时(session信息保存在服务器端).服务器会在响应头中设置一个
                sessionid 的cookie信息
            ④ 客户端(浏览器)在接收到响应之后,会将cookie信息保存起来(保存sessionid的信息)
        第二次及其之后的请求:
            ⑤ 第二次及其之后的请求都会携带 session id信息
            ⑥ 当服务器接收到这个请求之后,会获取到sessionid信息,然后进行验证,
                验证成功,则可以获取session信息(session信息保存在服务器端)
    2.效果
    
                
    3.从原理(http)角度
        第一次请求:
                ① 第一次请求,在请求头中没有携带任何cookie信息
                ② 我们在设置session的时候,session会做两件事.
                    # 第一件: 将数据保存在数据库中
                    # 第二件: 设置一个cookie信息,这个cookie信息是以 sessionid为key value 为xxx
                    cookie肯定会以响应的形式在响应头中出现
            第二次及其之后:
                ③ 都会携带cookie信息,特别是sessionid
"""


def set_session(request):
    """
    第一次请求:
            ① 我们第一次请求的时候可以携带一些信息(用户名/密码) cookie中没有任何信息
            ② 当我们的服务器接受到这个请求之后,进行用户名和密码的验证,验证没有问题可以设置
                session信息
            ③ 在设置session信息的同时(session信息保存在服务器端).服务器会在响应头中设置一个
                sessionid 的cookie信息
            ④ 客户端(浏览器)在接收到响应之后,会将cookie信息保存起来(保存sessionid的信息)
    :param request:
    :return:
    """
    # 1.
    print(request.COOKIES)
    # 2. 对用户名和密码进行验证
    # 假设认为  用户名和密码正确
    user_id = 666
    # 3. 设置session信息
    # request.session 理解为字典
    request.session['user_id'] = user_id
    
    # 4.返回相应
    return HttpResponse('set_session')


def get_session(request):
    """
     第二次及其之后的请求:
            ⑤ 第二次及其之后的请求都会携带 session id信息
            ⑥ 当服务器接收到这个请求之后,会获取到sessionid信息,然后进行验证,
                验证成功,则可以获取session信息(session信息保存在服务器端)
    :param request:
    :return:
    """
    # 1.请求都会携带 session id信息
    print(request.COOKIES)
    # 2. 会获取到sessionid信息,然后进行验证
    #    验证成功,则可以获取session信息(session信息保存在服务器端)
    # request.session 字典
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')
    # 业务逻辑
    
    # 3.返回响应
    return HttpResponse('get_session')


"""
登录页面
    GET 请求是获取 登录的页面
    POST 请求是    验证登录(用户名和密码是否正确)
"""


def show_login(request):
    return render(request)


def veri_login(request):
    return redirect('首页')


# 我想由2个视图
def login(request):
    # 我们需要区分业务逻辑
    if request.method == 'GET':
        return render(request)
    else:
        return redirect('首页')
    pass


"""
类视图 是采用面向对象的思路
    1.定义类视图
        ① 继承自 View (from django.views import View)
        ② 不同的请求方式有不同的业务逻辑
            类视图的方法 就是直接采用 http的请求名字,作为我们的函数名, 如:get ,post, put...
        ③ 类视图的方法的第二个参数 必须是请求实例对象
            类视图的方法  必须有返回值 返回值是HttpResponse及其子类
    
    2.类视图的url引导
"""

from django.views import View


class LoginView(View):
    
    def get(self, request):
        return HttpResponse('get')
    
    def post(self, request):
        return HttpResponse('post')
    
    def put(self, request):
        return HttpResponse('put')


"""
个人中心页面   --   必须登录才能显示
GET 方式 展示 个人中心
POST 实现个人中心信息的修改
定义类视图
"""
from django.contrib.auth.mixins import LoginRequiredMixin  # 登录验证


class CenterView(LoginRequiredMixin, View):  # 继承顺序不能改变
    
    def get(self, request):
        return HttpResponse('个人中心展示')
    
    def post(self, request):
        return HttpResponse('个人中心修改')


class HomeView(View):
    
    def get(self, request):
        
        # 1.获取数据
        uesrname = request.GET.get('username')
        
        # 2. 组织数据
        context = {
            'username': uesrname,
            'age': 12,
            'birthday': datetime.now(),
            'friends': ['Tom', 'Jack', 'Rose'],
            'score': {
                '2018': 80,
                '2019': 90,
                '2020': 99,
                '2021': 100,
            },
            'desc': '<script>alert("hot")</script>'
        }
        
        uesrname = request.GET.get('username')
        
        return render(request, 'index.html', context=context)
