#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/8 19:47
# @Author : Yang Peihao
# @Site : 
# @File : view.py.py
# @Software: PyCharm
from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello world!")