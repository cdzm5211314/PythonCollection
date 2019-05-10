# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的参数

'''
   定义函数时,小括号里面的变量称为形参
   调用该函数时,小括号里面传递进去的数据为实参 
   实参与形参的对应的
'''

# 定义一个函数,用来求两个数的和
# 函数调用时.传递进来的数据(实参)与定义函数中的变量(形参)是一一对应的(即参数个数与参数顺序都对应)
def add2num(x,y):
    sum = x + y
    print("两个数的和:sum = %d"%sum)
    print("%d + %d = %d"%(x,y,sum))
    # return sum :在函数中有return时,是把这个函数的结果返回回去,
    # 外界在调用这个函数时需要一个变量来接受这个函数返回的结果
    return sum

result1 = add2num(5,4)

# 调用函数时可以指定形参的值
result2 = add2num(x=4,y=5)

# 练习:计算1~ 的指定数据的累积和
def sumNums(endNum):
    i = 0
    sum = 0
    while i <= endNum:
        sum = sum + i
        i += 1
    return sum   
result = sumNums(5)
print(result)


