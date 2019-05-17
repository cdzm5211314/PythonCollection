# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### SQL语言:结构化查询语言,是一种数据库查询和程序设计语言,用于存取数据以及查询,更新和管理关系型数据库系统

### SQL语言可以做什么?
# 数据库数据的增删改查(CRUD)
# 数据库对象的创建,修改和删除
# 用户权限/角色的授权与取消
# 事务控制

### SQL语言的分类:
# -DQL(数据查询语言): 如 select
# -DML(数据操作语言): 如 insert ,update ,delete
# -DDL(数据定义语言): 如 create ,alert ,drop
# -DCL(数据控制语言): 如 grant ,revoke
# -TCl(事务控制语言): 如 savepoint ,rollback ,set transaction ,commit

# ********************************************************************* #

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

# ********************************************************************* #

### DML(数据操作语言): 如 insert ,update ,delete
# 插入数据:
    # 所有字段插入数据:  insert into 表名 values(...);
    # 插入某些字段数据: insert into 表名(列名1,列名2) values(值1,值2)
    # 插入多条数据: insert into 表名 values(...)(...)...
# 修改字段的值: update 表名 set 列名1=值1,列名2=值2 where 条件;
    # update test_table set tname='zhangsan' where id = 2
# 删除所有数据: delete from 表名;
    # delete from test_table;
# 删除某些数据: delete from 表名 where 条件
    # delete from test_table where id = 2 ;

# ********************************************************************* #

### DQL(数据查询语言): 如 select
# 查询一张表的所有数据: select * from 表名; ---> * 号表示该表的所有字段
    # select * from test_table;

# 查询一张表的某些字段数据: select 字段名1,字段名2 from 表名;
    # select id,tname from test_table;

# 给获取结果的列起别名:
    # select tname as 姓名 from test_table;
    # select tname 姓名 from test_table;

# 使用算术表达式: 比如表中一个员工工资字段sal,获取所有员工的年薪是多少
    # select tname,sal*12 from test_table;

# 使用distinct去掉重复的数据
    # select distinct 字段名 from 表名;

# 使用order by 对查询的结果进行排序: 默认是升序(asc),降序(desc)
    # select tname,sal from test_table order by sal     ---> 默认升序
    # select tname,sal from test_table order by sal desc    ---> 选择降序

### between ... and ... : 大于**** and 小于****(含有边界)
    # select name,english from student where english>=80 and english<=90;
    # select name,english from student where english between 80 and 90;

### in : 在集合中
    # select name,math from student where math=89 or math=90 or math=91;
    # select name,math from student where math in (89,90,91);

### like : 模糊查询     %:任意长度的任意字符串    _:任意的一个字符
    # select * from student where name like '李%';
    # select * from student where name like '__';

### limit : 分页查询
    # select * from test_table limit 0,5    ---> 从第一条数据开始,取5条数据
