# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

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