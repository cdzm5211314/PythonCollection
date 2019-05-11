# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-04-02 20:55

## 数据规约: 属性规约,数值规约

## 主成分分析: 安装: pip install sklearn
from sklearn.decomposition import PCA
import pymysql
import pandas

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="pythondb")
sql = "select hits,comment from myhexun"
data_sql = pandas.read_sql(sql, conn)

ch = data_sql[u"comment"] / data_sql["hits"]
data_sql[u"评点比"] = ch

# 主成分分析进行中
pca1 = PCA()
pca1.fit(data_sql)
# 返回模型中各个特征量
tz1 = pca1.components_
print(tz1)
# 各个成分中各自方差百分比，贡献率
rate = pca1.explained_variance_ratio_
print(rate)

pca2 = PCA(2)
pca2.fit(data_sql)
reduction = pca2.transform(data_sql)          # 降维
print(reduction)
recovery = pca2.inverse_transform(reduction)  # 恢复
print(recovery)


