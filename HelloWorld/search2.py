#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/9 11:14
# @Author : Yang Peihao
# @Site : 
# @File : search2.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# # 接收POST请求数据
# def search_post(request):
#     ctx = {}
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#     return render(request, "post.html", ctx)


# 表单
def tohtml(request):
    return render(request, 'post.html')

def search_post(request):
#  获取图片，此时该文件格式为二进制
    print("函数执行了。。。")
    commodity_image = request.FILES.get("commodityImage", None)
#  使用二进制的方式打开新建文件，不改变文件，直接写入
    with open("picture.jpg",mode="wb") as image_file:
        for content in commodity_image:
            image_file.write(content)
    return render(request, "post.html")