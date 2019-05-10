# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import os

### Python中的os模块可以进行对文件及目录的操作
# os.name() ---> 判断正在使用的平台,windows返回"nt",linux返回"posix"
# os.rename(需要修改的文件名,新的文件名)   ---> 也可以做剪切
# os.getcwd()   ---> 获取当前的工作目录
# os.listdir()  ---> 指定目录下的所有文件和目录名,以列表的形式全部列举出来,其中没有区分目录和文件
# os.remove()   ---> 删除指定文件
# os.rmdir()    ---> 删除指定目录
# os.mkdir()    ---> 创建目录:注意:只能创建一层
# os.makedirs() ---> 递归创建目录
# os.path.isfile()  ---> 判断指定对象是否是文件,是返回True,不是返回False
# os.path.isdir()  ---> 判断指定对象是否是目录,是返回True,不是返回False
# os.path.exists()  ---> 检验指定的对象是否存在,是返回True,不是返回False
# os.path.split()   ---> 返回路径的目录和文件名

### 修改文件的名字
# os.rename("text.txt","新文件.txt")

### 获取文件的绝对路径
print(os.path.abspath("新文件.txt"))

### 批量修改目录(test)下的文件名称
# 获取当前目录下列表
file_list = os.listdir("test/")
print(file_list)
for f in file_list:
    print(type(f))
    # 修改目标文件的文件名称
    dest_file = "re-" + f
    # 获取父目录的绝对路径
    parent_dir = os.path.abspath("test")
    # 文件的绝对路径 = 父目录的绝对路径 + / +文件名
    # os.path.join()    ---> 链接目录与文件名
    source_file = os.path.join(parent_dir,f)
    dest_file = os.path.join(parent_dir,dest_file)
    # os.rename("test/"+f,"test/"+dest_file)
    os.rename(source_file,dest_file)