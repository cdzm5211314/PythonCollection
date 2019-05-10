# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-14 15:07

class A:
    def test(self):
        print("A --- test")

    def demo(self):
        print("A --- demo")

class B:
    def test(self):
        print("B --- test")

    def demo(self):
        print("B --- demo")

class C(B, A):
    pass

# 在多继承的情况下,查看类的方法的执行顺序
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

