# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-17 9:49

import pymysql
import json

# 数据库信息及创建数据库:
"""
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "root",
    "db": "ShuangSeQiuDB",  
}
# 创建数据库: create database ShuangSeQiuDB default charset=utf8;
"""
# 创建数据库表:
"""
CREATE TABLE excel(
  id int(11) NOT NULL,
  redOne int(11) DEFAULT NULL,
  redTwo int(11) DEFAULT NULL,
  redThree int(11) DEFAULT NULL,
  redFour int(11) DEFAULT NULL,
  redFive int(11) DEFAULT NULL,
  redSix int(11) DEFAULT NULL,
  blueSeven int(11) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
"""


class MySQLHelper(object):

    def __init__(self, db_config):
        # 注: 创建对象的时候不链接数据库,再使用的时候才链接数据库
        self.connection = None
        self.cursor = None

    def query_all_list(self, sql, *args):  # 查询数据库所有行数据
        try:
            self.connection = pymysql.connect(**db_config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    def query_one_line(self, sql, *args):  # 查询数据库一行数据
        try:
            self.connection = pymysql.connect(**db_config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    def update_execute(self, sql, *args):  # 数据库的增,删,改操作
        try:
            self.connection = pymysql.connect(**db_config)
            self.cursor = self.connection.cursor()
            # 返回执行sql语句之后受影响的行数
            num = self.cursor.execute(sql, args)
            self.connection.commit()
            return num
        except Exception as ex:
            self.connection.rollback()
            print(ex)
        finally:
            self.close()

    def close(self):  # 关闭资源
        if self.cursor:  # 获取到了操作游标
            self.cursor.close()
        if self.connection:  # 数据库已链接
            self.connection.close()


if __name__ == '__main__':
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "root",
        "db": "ShuangSeQiuDB",
    }
    helper = MySQLHelper(db_config)
    # print(helper.connection)

    # sql = "select * from excel"
    # print(helper.query_all_list(sql))
    # print(helper.query_one_line(sql))

    # 根据id查询一条数据
    # sql = "select * from excel where id = %s"
    # print(helper.query_one_line(sql,1))

    # 删除数据库表
    # sql = "drop table excel"
    # print(helper.update_execute(sql))

    # 创建数据库表
    # sql = """CREATE TABLE excel(
    # id int(11) NOT NULL,
    # redOne int(11) DEFAULT NULL,
    # redTwo int(11) DEFAULT NULL,
    # redThree int(11) DEFAULT NULL,
    # redFour int(11) DEFAULT NULL,
    # redFive int(11) DEFAULT NULL,
    # redSix int(11) DEFAULT NULL,
    # blueSeven int(11) DEFAULT NULL,
    # PRIMARY KEY (id)
    # ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    # print(helper.update_execute(sql))

    # 批量插入数据(json)
    # 1. 逐条插入数据库数据,多次commit()操作: insert into 表名 values(...)
    # with open("双色球中奖数据保存.json", encoding="utf-8") as ft:
    #     ssq_list = ft.readlines()  # 读取json文件中的数据,获得json字符串组成的一个列表
    #     # print(ssq_list,type(ssq_list))
    #     for json_dict in [json.loads(json_str) for json_str in ssq_list]:  # 获得字典类型数据组成的一个列表并遍历
    #         print(json_dict, type(json_dict))
    #         # sql = "insert into excel values(json_dict['id'],json_dict['redOne'],json_dict['redTwo'],json_dict['redThree'],json_dict['redFour'],json_dict['redFive'],json_dict['redSix'],json_dict['blueSeven'])"
    #         sql = "insert into excel values(%s,%s,%s,%s,%s,%s,%s,%s)" % (
    #         json_dict['id'], json_dict['redOne'], json_dict['redTwo'], json_dict['redThree'], json_dict['redFour'],
    #         json_dict['redFive'], json_dict['redSix'], json_dict['blueSeven'])
    #         helper.update_execute(sql)

    # 2. 一次插入多条数据库数据: 一次commit()操作: insert into 表名 values(...)(...)...
    sql = "insert into excel values "
    with open("双色球中奖数据保存.json", encoding="utf-8") as ft:
        dict_list = [json.loads(json_str) for json_str in ft.readlines()]  # 把文件中json字符串转换为字典dict组成的数据列表
        # print(dict_list[0],type(dict_list[0]))
        for dict in dict_list:
            # json_tuple = tuple(dict.values())  # 遍历字典列表并把每个字典的value值组成一个元组
            json_tuple = str(tuple(dict.values()))  # 遍历字典列表并把每个字典的value值组成一个元组,再变成字符串
            # print(json_tuple)
            sql += json_tuple + ","
    # print(sql)
    # print(sql.rstrip(","))
    helper.update_execute(sql.rstrip(","))  # 去掉sql字符串最后面的,号






