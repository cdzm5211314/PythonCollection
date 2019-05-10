# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-18 10:42

# 每个模块都内置一个__file__属性,可以查看模块的完整路径

import random

# 获取0-9的随机数
rand = random.randint(0,9)

# 执行模块时,__name__的值永远为__main__
print(__name__)

if __name__ == "__main__":
    print(rand)

    print(random.__file__)
    # E:\Developer_Tools\PythonEnvs\python36\lib\random.py
    print(__file__)
    # E:/workspace_PyCharm/PythonDocs/[00]乱七八糟/模块内置属性__file__.py


