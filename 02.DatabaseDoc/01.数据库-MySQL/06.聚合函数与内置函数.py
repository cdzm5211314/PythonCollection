# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 聚合函数: count() ,max() ,min() ,sum() ,avg()
# count():表示求表中数据条数
# max(): 表示求某列的最大值
# min(): 表示求某列的最小值
# sum(): 表示求某列的和值
# avg(): 表示求某列的平均值

### MySQL内置函数:
# concat(): 字符串链接   ---> select concat(tname,'的工资是:',sal) from test_table;
# left(str,len): 返回字符串左端的len个字符
# right(str,len): 返回字符串右端的len个字符
# substring(str,pos,len): 返回字符串str的pos位置开始的len个字符
    # select substring("abc123",2,3)    ---> "c12"
# ltrim(str): 返回删左端空格的字符串
# rtrim(str): 返回删右端空格的字符串

### 把日期转换为字符串
    # DATE_FORMAT("日期","格式")   ---> DATE_FORMAT(CURRENT_DATE(),"%Y年%m月%d日")


