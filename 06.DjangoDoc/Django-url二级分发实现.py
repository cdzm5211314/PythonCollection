# -*- coding:utf-8 -*-
# @Desc : urls.py
# @Author : Administrator
# @Date : 2019-06-24 16:47

# 什么是url：http://127.0.0.1:8000/index/car/3?a=1
# 协议://IP:8000/路径?a=1&b=2

from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse

###
def test01(request):
    return HttpResponse("test01")

def test02(request):
    return HttpResponse("test02")

def test03(request):
    return HttpResponse("test03")

def test04(request):
    return HttpResponse("test04")

def test05(request):
    return HttpResponse("test05")

###
def list_view(request):
    return HttpResponse("list_view")

def add_view(request):
    return HttpResponse("add_view")

def change_view(request,id):
    return HttpResponse("change_view")

def delete_view(request,id):
    return HttpResponse("delete_view")

def get_urls_2():
    temp=[]
    temp.append(url(r"^$",list_view))
    temp.append(url(r"^add/$",add_view))
    temp.append(url(r"^(\d+)/change/$",change_view))
    temp.append(url(r"^(\d+)/delete/$",delete_view))
    return temp

def get_urls():
    print(admin.site._registry)  # {Book:modelAdmin(Book),.......}
    temp=[]
    for model,admin_class_obj in admin.site._registry.items():
        app_name=model._meta.app_label
        model_name=model._meta.model_name
        temp.append(url(r'^{0}/{1}/'.format(app_name,model_name), (get_urls_2(),None,None)),)
    return temp

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^index/$', test01),
    # 二级分发
    url("^yuan/",([
        url(r'^test01/', ([
            url(r'^test04/', test04),
            url(r'^test05/', test05),
        ],None,None)),
        url(r'^test02/', test02),
        url(r'^test03/', test03),
    ],None,None)),

    url(r'^Xadmin/', (get_urls(),None,None)),
    # 127.0.01:8000/Xadmin/app01/book/
    # 127.0.01:8000/Xadmin/app01/book/add
    # 127.0.01:8000/Xadmin/app01/book/1/change/
    # 127.0.01:8000/Xadmin/app01/book/1/delete/

]
