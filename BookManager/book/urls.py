#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: jmz
@file: urls.py
@time: 2020/11/19 9:39
@desc:
"""
from django.urls import path, re_path
from book.views import index, detail, set_cookie, get_cookie, set_session, get_session, LoginView, CenterView, HomeView

urlpatterns =[
    # index/
    # path 的第一个参数是：路径
    # path 的第二个参数是：视图函数名
    # path 的第三个参数是：给路由取个别名，可以通过name找到这个路由
    path('index/', HomeView.as_view(), name='index'),
    # 正则分组会传递参数给视图， 定义视图需要定义变量来接收参数
    # 关键字参数, 可以不用关系传递顺序
    re_path(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', detail),
    # cookie 的第一次请求
    re_path(r'^set_cookie/$', set_cookie, name='set_cookie'),
    # 第二次及其之后的请求
    re_path(r'^get_cookie/$', get_cookie),
    
    re_path(r'^set_session/$', set_session),
    re_path(r'^get_session/$', get_session),
    
    # 第二个参数是 视图的函数名
    re_path(r'login/$', LoginView.as_view()),
    re_path(r'center/$', CenterView.as_view()),
]