# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 当定义一个函数时,不确定它有几个参数时,就使用不定长参数;如 *args

def test1(x,y,*args):
    print(x,y)
    print(args)
    sum = x + y
    for i in args:
        sum += i
    print("几个数的和为: %s"%sum)

def test2(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
    sum = x
    for i in args:
        sum += i
    for i in kwargs.values():
        sum += i
    print("几个数的和为: %s"%sum)


test1(2,3,5,7,9,11)
# test2(10,20,30,num1 = 40,num2 = 50)

num1 = [20,30]
num2 = {"num1":40,"num2":60}
# 集合的拆包
test2(10,*num1,**num2)


# 不定长参数

# 如果定义函数不确定函数的形参有几个,可以在设置形参的最后一个前面加上*号
# 可传可不传的形参一定放在一定要传的形参的后面

def test(a,*b):
    print(a)
    print(b)

test(11,22,33,44,55)
# (22, 33, 44, 55)

def addAll(a,*b):
    result = 0
    result += a
    for x in b:
        result += x
    return result

# 调用函数时,传递不定长参数的值
res = addAll(1,2,3,4,5)
print(res)
# 15

def test2(a,*b,**c):
    print(a)
    print(b)
    print(c)
# 调用函数时,传递实参时指定值的名称
test2(11,22,33,m = 44,n = 55)
# 11
# (22, 33)
# {'m': 44, 'n': 55}










