# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 源文件路径
source_file = "D:/Pictures/5646.jpg"
# 目标路径
dest_file = "E:/Work_PyCharm/Python3_shangxuetang/[02]Python-函数操作/copy.jpg"

# 打开文件源文件
f = open(source_file,"rb")
# 读取源文件的内容并存放起来
textjpg = f.read()
# 打开要保存的文件
file = open(dest_file,"wb")
# 把源文件中读取的内容写到要保存的文件中
file.write(textjpg)
# 关闭文件
file.close()
f.close()