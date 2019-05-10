# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

#windows系统下：非关系型数据库MongoDB，客户端软件robo3t
# 安装pymongo: pip install pymongo

from pymongo import MongoClient

# 创建链接
client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://localhost:27017/")

# 获取数据库(test)
db = client.test
# db = client['test']

# 获取集合[即表](person)
collection = db.person
# collection = db['person']

# 操作数据库中的集合[即表]文档[即数据]:
#pass  #(CRUD增删改查)

# 添加一个文档
# collection.insert({"name":"张三","age":35,"address":"重庆"})
# 添加多个文档
# collection.insert([{"name":"abc1","age":15,"address":"重庆"},{"name":"abc2","age":20,"address":"tianjin"}])

### 查询文档
# 条件查询
# res = collection.find({"age":{"$gt":25}})
# print(res)
# for coll in res:
#     print(coll)
# print(type(coll))

# 查询所有
# res = collection.find().count()
# for coll in res:
#     print(res)

# 统计查询
# res = collection.find({"age":{"$gt":25}}).count()
# print(res)

# 根据id查询，需要导入模块
# from bson.objectid import ObjectId  # 用于id查询
# res = collection.find({"_id":ObjectId("5af1072e8fdd1b19e8a4d149")})
# print(res[0])

# 排序
# res = collection.find({"age":{"$gt":25}}).sort("age")  # 升序
# res = collection.find({"age":{"$gt":25}}).sort("age",pymongo.DESCENDING)  # 降序
# for s in res:
#     print(s)

# 分页
# res = collection.find().skip(8).limit(4)
# for f in res:
#     print(f)

# 更新文档 : 把name值为777的文档的age属性改为10
# collection.update({"name":"777"},{"$set":{"age":"10"}})

# 删除文档：删除name属性值为777的数据
collection.remove({"name":"777"})
# 删除全部
collection.remove()

# 断开或关闭链接
client.close()


