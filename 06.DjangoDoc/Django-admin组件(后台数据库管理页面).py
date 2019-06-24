# -*- coding:utf-8 -*-
# @Desc : admin.py文件
# @Author : Administrator
# @Date : 2019-06-21 15:11

### 管理站点(admin): 注册账号
# python manage.py createsuperuser
# Username: admin # 输入你要创建的用户名
# Email address: admin@163.com # 输入你的邮箱,可以不写
# Password: admin # 输入你的密码
# Password(again): admin # 再次输入你的密码

### setting.py设置要使用的数据库类型
# 配置mysql数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # 使用的数据库类型
#         'NAME': 'pythondb',  # 数据库名称
#         'HOST': 'localhost',  # IP地址
#         'POST': 3306,  # 端口号
#         'USER': 'root',  # 用户名
#         'PASSWORD': 'root',  # 密码
#     }
# }

### 1.在app应用下models.py中定义模型类
# from django.db import models
# class Book(models.Model):
#     name = models.CharField(max_length=64)
#     author = models.CharField(max_length=20)

### 2.生成迁移文件,执行迁移文件
# python manage.py makemigrations
# python manage.py migrate

### 3.在app应用下admin.py中完成模型类注册
# 导入你要注册的模型类
# from django.contrib import admin
# from .models import Book
# admin.site.register(Book)  # 注册

# 自定义数据库管理页面并注册:
# 管理站点页面在此可以任意的设置: 如 list_display ,list_display_link ,list_filter ...
from django.contrib import admin
from django.utils.safestring import mark_safe
# from .models import Book
# @admin.register(Book)  # 简写注册
class BookAdmin(admin.ModelAdmin):
    def deletes(self):
        return mark_safe("<a href=''>删除</a>")
    list_display = ["name", "author",deletes]  # 定制显示的列: 展示模型字段或自定义函数名称
    list_display_link = ["author"]  # 定制列可以点击跳转: 点击哪个字段进入编辑页面
    list_filter = ["author"]  # 定制右侧快速筛选栏: 根据字段过滤
    search_fields = ["name"]  # 定制快速搜索栏:
    ## 批量操作
    def patch_init(self, request, queryset):
        queryset.update(name = "zhangsan")
    patch_init.short_description = "批量初始化name的名字"
    actions = ["patch_init"]
# admin.site.register(Book, BookAdmin)  # 注册






