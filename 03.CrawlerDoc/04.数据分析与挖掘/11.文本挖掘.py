# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2019-04-02 21:29

# 文本数据挖掘(Text Mining): 是指从文本数据中抽取有价值的信息和知识的计算机处理技术
# 安装: pip install jieba
import jieba

sentence = "我喜欢上海东方明珠"

# cut()默认使用精准模式
# 全模式切分
text1 = jieba.cut(sentence, cut_all=True)
# for t in text1:
# print(t)

# 精准模式切分
text2 = jieba.cut(sentence, cut_all=False)
# for t in text2:
#     print(t)

# 示例: 搜索引擎模式切分
text3 = jieba.cut_for_search(sentence)
# for t in text3:
#     print(t)

#######################################################

## 词性标注
# 属性word: 词语
# 属性flag: 词性
"""
a: 形容词
c: 连词
d: 副词
e: 叹词
f: 方位词
i: 成语
m: 数词
n: 名词
nr: 人名
ns: 地名
nt: 机构团体
nz: 其他专有名词
p: 介词
r: 代词
t: 时间
u: 助词
v: 动词
vn: 名动词
w: 标点符号
un: 未知词语
"""
import jieba.posseg

text4 = jieba.posseg.cut(sentence)
# for t in text4:
#     print(t.word + " ---> " + t.flag)

# 示例: 加载创建的新词典
jieba.load_userdict("E:/Developer_Tools/PythonEnvs/py3scrapy/Lib/site-packages/jieba/dict2.txt")

# 更改词频
sentence2 = "韬云科技是做云计算的"
text5 = jieba.cut(sentence2)
# for t in text5:
#     print(t)
# 发现云与计算是切分的,要更改成云计算出现一次
# jieba.add_word("云计算")
jieba.suggest_freq(("云", "计算"), True)
text6 = jieba.cut(sentence2)
# for t in text6:
#     print(t)

#############################################################

## 返回文本中出现比较多的
import jieba.analyse

sentence3 = "我喜欢上海东方明珠"
# 提取关键词
tag = jieba.analyse.extract_tags(sentence3, 3)
# print(tag)
# 返回词语的位置
w9 = jieba.tokenize(sentence3)
# for item in w9:
#     print(item)

w10 = jieba.tokenize(sentence3, mode="search")
# for item in w10:
#     print(item)

######################################################
# 示例: 分析血尸的词频
data = open("血尸.txt",encoding="utf-8").read()
tag = jieba.analyse.extract_tags(data, 15)
# print(tag)

# 示例: 盗墓笔记的关键词提取
# 编码问题解决方案
data=open("盗墓笔记.txt","r",encoding='utf-8').read()
import urllib.request
tag = jieba.analyse.extract_tags(data, 30)
# print(tag)
