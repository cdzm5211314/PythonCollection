# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-16 15:55


# assert 断言,后面跟一个表达式
# 如果表达式为真,则断言成功,程序往下执行
# 如果表达式为假,则断言失败,程序终止执行,会抛出异常AssertionError


def num_div(num1, num2):
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1 / num2)


if __name__ == '__main__':
    # num_div(10, "b")  # 抛出异常: AssertionError
    # num_div(20, 0)    # 抛出异常: ZeroDivisionError: division by zero
    num_div(20, 2)





