# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-18 14:47

# 语法: eval(expression[, globals[, locals]])
# 参数:
    # expression -- 表达式。
    # globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    # locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象

# eval()函数 接受字符串参数, 将字符串 当成 有效的表达式 求值,并返回结果

print(eval("1 + 3"))  # 4

print(type(eval("{'name':'zhangsan','age':18}")))  # dict

# 计算器案例
input_str = input("请输入算术题: ")
print(eval(input_str))

# 注: 在开发时不要使用eval()函数转换input的结果

# __import__('模块名称')   # 导入模块
__import__('os').system('ls')
# 代码等价于如下代码
import os
os.system('终端命令')

# 执行成功,返回0
# 执行失败,返回报错信息

eval("__import__('os').system('删除命令')")   # 不安全