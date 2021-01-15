#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: jmz
@file: jinja2_env.py
@time: 2021/1/15 16:31
@desc:
"""
from django.template.defaultfilters import date
from jinja2 import Environment

def environment(**option):
    # 1.创建 Environment实例
    env = Environment(**option)
    # 2. 指定(更新) jinja2的函数指向Django的指定过滤器
    env.globals.update({
        'date': date
    })
    # 3. 返回Environment实例
    return env