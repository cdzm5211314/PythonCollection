# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### windows系统下：关系型数据库MySQL，客户端软件Navicat for MySQL
import pymysql


class MySQLHelper(object):
    config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "db": "chenssq"
    }

    def __init__(self):
        self.connection = None
        self.cursor = None

    # 从数据库表中查询一行数据
    def getOne(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex, ex)
        finally:
            self.close()

    # 从数据库表中查询所有行数据
    def getList(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex, ex)
        finally:
            self.close()

    # 对数据库进行增,删,改
    def executeDML(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            # 返回执行sql语句之后受影响的行数
            num = self.cursor.execute(sql, args)
            self.connection.commit()
            return num
        except Exception as ex:
            self.connection.rollback()
            print(ex, ex)
        finally:
            self.close()

    # 关闭资源
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


# 测试
if __name__ == "__main__":
    helper = MySQLHelper()
    # print(helper.executeDML("delete from test_table where id = 6"))
    print(helper.executeDML("delete from test_table where id = %s", 5))
