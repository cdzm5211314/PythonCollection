# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import pymysql

connection = None
cursor = None
try:
    # 创建Connection对象,自动开启事务
    connection = pymysql.connect("localhost","root","root","test")
    # 创建Cursor对象
    cursor = connection.cursor()
    # sql语句
    # sql = "insert into test_table values(4,'liuliu')"
    # sql = "insert into test_table values(%s,'%s')"%(5,"xuqi")
    sql = "insert into test_table values(%s,%s)"
    try:
        # cursor执行sql语句,返回一个受影响的数据条数
        # cursor.execute(sql)
        cursor.execute(sql,(6,"jiangba"))
        connection.commit()
    except Exception as ex:
        connection.rollback()
        print(ex)
except Exception as ex:
    print(ex)
finally:
    # 关闭游标和连接
    if cursor:
        cursor.close()
    if connection:
        connection.close()
