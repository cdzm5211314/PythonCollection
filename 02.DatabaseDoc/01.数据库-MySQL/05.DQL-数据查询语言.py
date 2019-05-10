# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

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





