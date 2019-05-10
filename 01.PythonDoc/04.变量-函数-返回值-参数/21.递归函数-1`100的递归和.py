# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23


# 递归练习:求1~100的递归的和

def test(num):
    if num > 1:
        result = num + test(num-1)
    else:
        result = 1
    return result  

result = test(100)
print(result)





