# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

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







