# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 表连接: 内连接 与 外连接 ---> (两张表有连接关系如:一张表的主键与另张表的外键)

# 内连接:
    # select table1.column, table2.column from table1, table2 where table1.column = table2.column
    # select table1.column, table2.column from table1 inner join table2 on table1.column = table2.column
    # 自连接:(一张表)
        # select t1.column, t2.column from table as t1 join table as t2 on t1.column1 = t2.column2

# 外连接: 左外连接 与 右外连接 与 满外连接
    # 左外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回左表中不满足条件的行
        # select table1.column, table2.column from table1 left join table2 on table1.column = table2.column

    # 右外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回右表中不满足条件的行
        # select table1.column, table2.column from table1 right join table2 on table1.column = table2.column

    # 满外连接:两个表在连接过程中除返回满足连接条件的行以外,还返回两个表中不满足条件的所有行
        # select table1.column, table2.column from table1 full join table2 on table1.column = table2.column


### 子查询:
# 子查询语法格式:
    # select 字段列表 from table where 表达式 operator (select 字段列表 from table)
# 子查询特点:
    # 子查询在主查询前执行一次
    # 主查询使用子查询的结果
# 单行子查询: 返回的只有一记录
    # 对单行子查询可使用单行记录比较运算符: 如: <, >, =, >=, <=, <>, !=
# 多行子查询:返回的有多条记录
    # 对多行子查询只能使用多行记录比较运算符: 如:
        # all 和 子查询返回的所有值比较
        # any 和 子查询返回的任意值比较
        # in 等于列表中的任何一个





