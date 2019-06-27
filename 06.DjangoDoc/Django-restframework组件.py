# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-27 9:33

### restful: 是一个协议
# 一切皆资源,操作只是请求方式

### Django - restframework框架: 针对的为json数据
# 安装django: pip install django
# 安装restframework: pip install djangorestframework

### restframework 序列化:
# views.py ---> 序列化数据
from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.views import APIView
class PublishView(View):
    def get(self,request):
        # 序列化方式一：json模块
        # import json
        # publish_list = list(Publish.objects.all().values("name","email"))
        # return HttpResponse(json.dumps(publish_list))

        # 序列化方式二：django-crm内置序列化方法
        # from django.forms.models import model_to_dict
        # publish_list=Publish.objects.all()
        # temp=[]
        # for obj in publish_list:
        #     temp.append(model_to_dict(obj))
        # return HttpResponse(temp)

        # 序列化方式三：django内置的序列化组件
        # from django.core import serializers
        # result = serializers.serialize("json",publish_list)
        # return HttpResponse(result)

        # 序列化方式四: 使用restframework组件序列化数据: 定义类并继承restframework组件中的Serializer类
        # publish_list = Publish.objects.all()
        # ps = PublishSerializers(publish_list, many=True)  # queryset数据
        # ps = PublishSerializers(publish_obj)              # model对象
        # return HttpResponse(ps.data)
        pass

# 使用restframework组件序列化数据
# 1. 定义类继承restframework组件中的Serializer类
from rest_framework import serializers
class PublishSerializers(serializers.Serializer):
    """ 此类是为QuerySet,model对象做序列化 """
    # 定义需要序列化的字段
    name = serializers.CharField()
    email = serializers.CharField()


# 待续...

