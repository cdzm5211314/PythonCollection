# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-04-02 20:55

import pymysql
import pandas

conn = pymysql.connect(host="127.0.0.1", user="root", passwd='root', db='pythondb')
sql = "select * from myhexun"
data_sql = pandas.read_sql(sql, conn)
# print(data_sql)
# 示例: 计算得到一个评点比: 评论数/点击数
ch = data_sql[u'comment']/data_sql[u'hits']
print(ch)
# 构造属性
data_sql[u'评点比'] = ch
# 把构造好的属性写进文件中
file = "./pdb.xls"
data_sql.to_excel(file,index=False)   # file表示文件,index表示索引,此处设置为Flase表示没有
# 此处报错: ModuleNotFoundError: No module named 'xlwt'
# 需要安装: pip install xlwt


