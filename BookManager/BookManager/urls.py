"""
路由相关

BookManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
1.urlpatterns 是固定写法，他的值是  列表
2.我们在浏览器中输入的路径会和 urlpatterns中每一项顺序进行匹配
    如果匹配成功，则直接引导到响应的模块.
    如果匹配不成功(把urlpatterns中的每一个都匹配过)，则直接返回404.
3.urlpatterns中的元素是 url
    url的第一个参数是：正则
        r 转义
        ^ 严格的开始
        $ 严格的结尾
        url(r'^admin/', admin.site.urls),
4.我们在浏览器中输入的路由中哪些部分参与正则匹配？
    http://ip:port/?key=value
    我们的http://ip:port/ 和 get、post参数不参与正则匹配
5.如果和当前的某一项匹配成功，则引导到子应用中继续匹配
    如果匹配成功，则停止匹配并返回相应的视图
    如果匹配不成功，则继承和后面的工程中的url的每一项继续匹配
6.

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 添加一项，只要不是 admin/ 肯定会走这个
    # 在include 的第二个三叔中添加一个namespace
    # 这样的话 name就变成了namespace:name
    # namespace 习惯上使用 子应用的名字
    path('', include(('book.urls','book'), namespace='book')),
    
    path('pay/', include('pay.urls')),
    
    
]
