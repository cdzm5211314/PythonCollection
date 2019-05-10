# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import os

### 案例:从某个目录(E:/Work_PyCharm/Python3_shangxuetang/[02]Python-函数操作/test/)下查找包含hello的py文件有哪些?
file_list = []
# 递归函数---使用绝对路径:parent_dir:文件所在父目录的绝对路径,file_name:当前你要处理的文件或目录
def find_hello(parent_dir,file_name):
    # 拼接你当前处理的文件或目录的绝对路径
    file_abspath = os.path.join(parent_dir,file_name)
    # 首先判断是否是一个目录
    if os.path.isdir(file_abspath):  # 如果传入的是一个目录
        for f in os.listdir(file_abspath):  # 进入目录,列表该目录下的所有文件列表
            find_hello(file_abspath,f)  # 递归调用自己本身的函数
    else:
        # 如果传入的是一个文件,判断文件名是否是以.py结尾
        if file_abspath.endswith(".py"):
            # 读取该.py结尾的文件,查看内容中是否含有hello
            if read_and_find_hello(file_abspath):
                file_list.append(file_abspath)

# 读取.py结尾的文件,查看内容是否有hello
def read_and_find_hello(py_file):
    flag = False
    # 打开文件
    file = open(py_file)
    while True:
    # 查看文件内容是否含有hello
        line = file.readline()
        if line == "":  # 如果文件读取完成(最后一行),退出循环
            break
        elif "hello" in line:  # 查找到
            flag = True
            break
    # 关闭文件
    file.close()
    return flag


# print(read_and_find_hello("test/file2.py"))
find_hello("E:/Work_PyCharm/Python3_shangxuetang/[02]Python-函数操作","test")
print(file_list)