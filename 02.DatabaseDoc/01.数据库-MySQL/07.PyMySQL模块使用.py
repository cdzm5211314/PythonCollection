# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import pymysql

### Python程序中使用MySQL数据库,需要安装导入PyMySQL模块
# 安装PyMySQL模块: pip install PyMySQL
# 导入PyMySQL模块: import pymysql

# Connection对象: 用于建立与数据库的链接
# 创建Connection对象: pymysql.connect(参数列表)
    # 参数列表:
        # host: 连接的MySQL主机地址,如果是本机就是localhost
        # port: 连接的MySQL主机端口号,默认是3306
        # db: 数据库名称
        # user: 连接的用户名
        # password: 连接的用户名的密码
        # charset: 通信采用的编码方式,默认是"gb2312",要求与数据库创建时指定的编码一致,否则中文会乱码
# Connection对象的方法:
    # close(): 关闭连接
    # commit(): 事务提交
    # rollback(): 事务回滚,放弃之前的操作
    # cursor(): 返回Curour对象,用于执行SQL语句并获得结果

# Curour对象: 执行SQL语句
# 创建Curour对象: Connection对象.cursor()
# Curour对象的方法:
    # close(): 关闭
    # execute(operation [,parameters]): 执行语句,返回受影响的行数
    # fetchone(): 执行查询语句时,获取查询结果集的第一行数据,返回一个元组
    # fetchall(): 执行查询语句时,获取查询结果集的所有,一行构成一个元组,再将这些元组装入另一个元组中返回
    # next(): 执行查询语句时,获取当前行的下一行
    # scroll(value [,mode]): 将行指针移到某个位置
        # model:表示移动的方式
        # model的默认值为relative,表示基于当前行移动到value,value为正是向下移动,value为负是向上移动

# ******************************************************************************************************* #

import pymysql

# 创建Connection对象
connection = pymysql.connect("localhost","root","root","test")

# 创建Cursor对象
cursor = connection.cursor()

# sql语句
sql = "select * from test_table"

# cursor执行sql语句,返回一个受影响的数据条数
num = cursor.execute(sql)
print(num)

# 获取cursor执行sql语句后的结果集的第一行数据(列表形式)
tuple = cursor.fetchone()
print(tuple)

# 获取cursor执行sql语句后的结果集的所有行数据(列表形式)
tuple = cursor.fetchall()
print(tuple)

# 关闭游标和连接
cursor.close()
connection.close()



