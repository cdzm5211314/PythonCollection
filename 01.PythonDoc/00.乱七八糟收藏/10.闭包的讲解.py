# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-05-01 19:43

### 内部函数对外部函数作用域里变量的引用(非全局变量),则称内部函数为闭包

# 定义一个函数
def test(number):
    # 在函数内部在定义一个函数,并且这个函数用到了外部函数的变量
    def test_in(number_in):
        return number + number_in
    # 其实这里返回的就是闭包的结果
    return test_in

print(test(10)(20))


