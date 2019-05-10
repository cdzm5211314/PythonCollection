# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### DDL(数据操作语言): 如 create ,alert ,drop
# 创建数据库:
    # create database 数据库名称;
# 删除数据库:
    # drop database 数据库名称;
# 进入数据库:
    # use 数据库名称;
# 查看当前选择的数据库:
    # show databases;
# 查看当前数据库中的所有表:
    # show tables;
# 创建表: create 表名(列名,类型);    auto_increment:表示主键自动增长
    # create test_table(
    #   id int auto_increment primary key,
    #   tname varchar(20) not null
    # );
# 查询表结构:
    # desc 表名
# 查看表的创建语句:
    # show create table 表名;
# 修改表名:
    # rename table 原表名 to 新表名;
# 修改表:  alert table 表名 add|change|drop 列名 类型;
    # 给表添加字段: alert table 表名 add 新加字段名称 新加字段类型;
        # alert table test_table add birthday datetime;
    # 修改表中的字段: alert table 表名 change 要修改的字段名 修改后的字段名 修改后的字段类型;
        # alert table test_table change r_name d_name varchar(32);
    # 删除表中的字段: alert table 表名 drop 要删除的字段名;
        # alert table test_table drop sex;
# 删除表:
    # drop table 表名;

