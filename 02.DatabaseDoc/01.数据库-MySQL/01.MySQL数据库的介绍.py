# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### MySQL是一个关系型数据库管理系统
### MySQL所使用的SQL语言是用于访问数据库的最常用标准化语言

### MySQL数据库安装后的链接
# 配置配置系统环境变量:   path = 安装目录/bin;
# 命令行终端链接本地数据库: mysql -u 用户名 -p  ---> 回车,然后输入密码
# 命令行终端链接远程数据库: mysql -h 远程ip地址 -u 用户名 -p   --->回车,然后输入密码
# 解决MySQL数据库中的乱码问题: default-character-set = utf8

# 使用命令行终端进入数据库后mysql的函数:
    # 查看数据库版本:  select version();
    # 查看当前系统时间:   select now();
    # 退出mysql数据库: quit 或 exit

# 使用命令行终端进入数据库后的简单操作:
    # 创建一个新的数据库:  create database 数据库名称;
    # 查看所有数据库:  show databases;
    # 进入其中的某个数据库:   use 数据库名称;
    # 查看进入的数据库中的所有表:   show tables;

# 使用命令行终端创建一个MySQL用户:
    # create user 用户名@localhost identified by '密码'; ---> localhost本地访问
    # create user 用户名@% identified by '密码'; ---> %具有远程访问

# 使用命令行终端给创建的用户授权:
    # grant all on 数据库名称.* to 用户名@%;

# 使用命令行终端备份(导出)数据: mysqldump -u 用户名 -p 数据库名 > 本地目录位置\导出的文件名称.sql    ---> 回车,输入密码
    # mysqldump -u root -p test > c:\test.sql

# 使用命令行终端恢复(导入)数据: mysql -u 用户名 -p 数据库名 < 本地目录位置\导入的文件名称.sql    ---> 回车,输入密码
    # mysql -u root -p test < c:\test.sql

# 如果存在一个sql脚本文件,直接执行该文件
    # source sql脚本文件路径
