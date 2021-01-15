#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: jmz
@file: urls.py
@time: 2020/11/19 10:29
@desc:
"""
from pay.views import order
from django.urls import path

urlpatterns =[
    path('order/', order)
    
]