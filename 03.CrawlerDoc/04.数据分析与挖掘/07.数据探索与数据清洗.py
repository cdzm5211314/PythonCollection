# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-03-30 22:22

# 数据探索的核心:
# 1. 数据质量分析(跟数据清洗密切联系)
# 2. 数据特征分析(分布,对比,周期性,相关性,常见统计量等)

# 数据清洗的步骤:
# 1. 缺失值处理(通过describe()与len()直接发现,通过0数据发现)
# 2. 异常值处理(通过散点图发现)

# 一般遇到缺失值,处理方式为:删除,插补,不处理
# 一般遇到异常值,处理方式为:缺失值,删除,修补(平均数,中位数),不处理
# 插补的方式主要有: 均值插补,中位数插补,众数插补,固定值插补,最近数据插补,回归插补,拉格朗日插值,牛顿插值法,分段插值等等

import pymysql
import numpy
import pandas
from matplotlib import pylab
""""
CREATE TABLE IF NOT EXISTS `taob` (
  `title` VARCHAR(50) DEFAULT NULL,
  `link` VARCHAR(60) NOT NULL,
  `price` INT(30) DEFAULT NULL,
  `comment` INT(30) DEFAULT NULL,
  PRIMARY KEY (`link`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8;

INSERT INTO `taob` (`title`, `link`, `price`, `comment`) VALUES
('买2袋减2元 印尼进口菲那菲娜虾味木薯片油炸大龙虾片零食品400g', 'https://item.taobao.com/item.htm?id=44350560220', 50, 2577),
('零食大礼包送女友一箱整箱好吃的休闲小吃组合混合装生日吃货进口', 'https://item.taobao.com/item.htm?id=528296696972', 116, 286692),
('牛肉干内蒙古牛肉粒特产零食手撕五香牛肉粒干片500g克包邮xo酱烤', 'https://item.taobao.com/item.htm?id=539655516205', 88, 567),
('爱尝泡鸭爪鸭掌福建龙岩特产下洋土楼卤味零食香辣泡爽泡椒泡爪', 'https://item.taobao.com/item.htm?id=520224855651', 118, 30664),
('30包湖南特产显峰嚼味鱼霸香辣小鱼仔麻辣零食鱼干口水毛毛鱼', 'https://item.taobao.com/item.htm?id=44752472349', 40, 6543),
('11月25日生产 正宗友臣肉松饼2.5kg整箱福建特产糕点心5斤零食品', 'https://item.taobao.com/item.htm?id=522922344354', 85, 1446),
('京辉爱面子点心面27g*20袋干脆面干吃面方便面办公室休闲零食包邮', 'https://item.taobao.com/item.htm?id=537650895010', 20, 592),
('好吃的手撕风干牛肉干内蒙古牛肉条原味散装零食品特产牛肉干500g', 'https://item.taobao.com/item.htm?id=537758670507', 158, 9878),
('特价进口俄罗斯巧克力kpokaht紫皮糖果婚庆喜糖零食品 原包装2斤', 'https://item.taobao.com/item.htm?id=36834424616', 60, 30834),
('靖江猪肉脯500g小吃特价零食猪肉干猪肉铺猪肉片蜜汁肉干一件包邮', 'https://item.taobao.com/item.htm?id=528461840334', 96, 36183),
('湛江风味特产新顺铁板烧鱿鱼片500g即食海鲜零食小吃干货鱿鱼丝条', 'https://item.taobao.com/item.htm?id=22208660649', 79, 3425),

"""

conn = pymysql.connect(host="127.0.0.1",user = "root",passwd = "root",db = "pythondb")
sql = "select * from taob"
data_sql = pandas.read_sql(sql,conn)  # 读取数据库数据
# print(data_sql)
'''
                                      title  ... comment
0         买2袋减2元 印尼进口菲那菲娜虾味木薯片油炸大龙虾片零食品400g  ...    2577
1            零食大礼包送女友一箱整箱好吃的休闲小吃组合混合装生日吃货进口  ...  286692
2         牛肉干内蒙古牛肉粒特产零食手撕五香牛肉粒干片500g克包邮xo酱烤  ...     567
'''

### 清洗数据
print(data_sql.describe())  # 统计数据
# 发现缺失值: 待续...

# 异常值处理:画散点图(x轴为价格,y轴为评论数)
data = data_sql.T  # 转置一下数据
# print(data,type(data))
'''
                                                    0     ...                                              9615
title                  买2袋减2元 印尼进口菲那菲娜虾味木薯片油炸大龙虾片零食品400g  ...                    天天特价干吃汤圆爆浆麻薯好吃的糯米糍麻糍米糕小吃糕点特产零食
link     https://item.taobao.com/item.htm?id=44350560220  ...  https://item.taobao.com/item.htm?id=533227194958
price                                                 50  ...                                                90
comment                                             2577  ...                                              7549
'''
# 得到价格和评论数
price = data.values[2]
comment = data.values[3]
# 画散点图polt
pylab.plot(price,comment,'o')
pylab.show()
# 异常值处理,价钱>2300的为异常值,评论数>200000的为异常值
line = len(data_sql.values)         # 从数据库读取出来的有多少条数据
column = len(data_sql.values[0])    # 从数据库读取的数据是多多少列
data1 = data_sql.values             # 把从数据库读取的数据变成二维数组
for i in range(0,line):  # 循环遍历每条记录
    for j in range(0,column):  # 循环遍历每条记录的元素
        if data1[i][2] > 200:  # 筛选每条记录的价格大于2300的
            # print(data1[i])
            data1[i][2] = 36    # 设置价格price的异常值为中位数

        if data1[i][3] > 10000:  # 筛选每条记录的评论数大于2300的
            # print(data1[i])
            data1[i][3] = 58    # 设置价格评论数的异常值为中位数
# print(data1,type(data1))
data1_t = data1.T  # 在转置下处理后的数据
# print(data1_t,type(data1_t))
price_t = data1_t[2]      # 取出处理异常值后的价钱
comment_t = data1_t[3]    # 取出处理异常值后的评论数
pylab.plot(price_t,comment_t,'o')
pylab.show()

### 分布分析:直方图
# 极差: 最大值 - 最小值
# 组距: 极差 / 组数(自定义)
# 得到价格和评论的最大值与最小值
price_max = data1_t[2].max()
price_min = data1_t[2].min()
comment_max = data1_t[3].max()
comment_min = data1_t[3].min()
# 计算出价格和评论数的极差和组距
price_jicha = price_max - price_min
comment_jicha = comment_max - comment_min
price_zuju = price_jicha / 12
comment_zuju = comment_jicha / 12
print(price_zuju,comment_zuju)
# 画价格的直方图(以价格的最小值price_min开始,以价格最大值price_max结束,间隔为价格的组距price_zuju)
price_style = numpy.arange(price_min,price_max,price_zuju)
pylab.hist(data1_t[2],price_style)
pylab.show()
# 画价格的直方图(以价格的最小值price_min开始,以价格最大值price_max结束,间隔为价格的组距price_zuju)
comment_style = numpy.arange(comment_min,comment_max,comment_zuju)
print(comment_style)
pylab.hist(data1_t[3],comment_style)
pylab.show()


