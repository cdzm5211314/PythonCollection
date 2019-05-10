# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-01-09 17:58

# JSON支持数据格式:
# 1. 对象(字典),使用{}
# 2. 数组(列表),使用[]
# 3. 整形,浮点型,布尔类型,null类型
# 4. 字符串类型(字符串必须要用双引号,不能使用单引号)
# 多个数据之间用哪个逗号分开,注:json本质上就是一个字符串

import json

books_dict = {
    "1":{
        "title": "十万个为什么",
        "price": 49
    },
    "2":{
        "title": "学习Python编程",
        "price": 49
    }
}
books_list = [
    {
        "title": "十万个为什么",
        "price": 49
    },
    {
        "title": "学习Python编程",
        "price": 49
    }
]
# print(books_dict,type(books_dict))  # <class 'dict'>
# print(books_list,type(books_list))  # <class 'list'>

### json.dumps()把Python数据转换成Json字符串
# 字典类型数据转换成Json数据
json_str1 = json.dumps(books_dict,ensure_ascii=False)
# print(json_str1,type(json_str1))  # <class 'str'>
# 字典类型数据转换成Json数据
json_str2 = json.dumps(books_list,ensure_ascii=False)
# print(json_str2,type(json_str2))  # <class 'str'>

### json.dump()把Python数据[字典]写入到文件中
with open("response_dict.json","w",encoding='utf-8') as fp:
    json.dump(books_dict,fp,ensure_ascii=False)  # 把字典类型数据直接写入到文件中
    # fp.write(json_str1)  # 把转换成json的数据写入文件中

### json.dump()把Python数据[列表]写入到文件中
with open("response_list.json","w",encoding='utf-8') as fp:
    json.dump(books_list,fp,ensure_ascii=False)  # 把字典类型数据直接写入到文件中
    # fp.write(json_str2)  # 把转换成json的数据写入文件中

### Json数据转换成字典,列表: json.loads()
# Json数据转换成字典类型
json_dict = json.loads(json_str1)
# print(json_dict,type(json_dict))
# Json数据转换成列表类型
json_list = json.loads(json_str2)
# print(json_list,type(json_list))

### json.load()把文件中的数据提取出来转换成Python数据[字典]
with open("response_dict.json",encoding='utf-8') as fp:
    fp_dict = json.load(fp)  # 使用json从文件中读取出来的数据为Python数据格式[与写入时的数据类型一致]
    # fp_dict = fp.read()  # 使用文件对象从文件中读取出来的数据为str字符串类型
    # print(fp_dict,type(fp_dict))

### json.load()把文件中的数据提取出来转换成Python数据[列表]
with open("response_list.json",encoding='utf-8') as fp:
    fp_list = json.load(fp)  # 使用json从文件中读取出来的数据为Python数据格式[与写入时的数据类型一致]
    # fp_list = fp.read()  # 使用文件对象从文件中读取出来的数据为str字符串类型
    # print(fp_list, type(fp_list))



##########################################################################################################
# import requests
# from pprint import pprint  # 格式化输入内容
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
# url = 'http://httpbin.org/get'
# response = requests.get(url, headers=headers)
# result = response.content.decode("utf-8")
# print(result, type(result))  # str

# json.loads把json字符串转换为python数据类型
# dict_py = json.loads(result)  # dict
# print(dict_py, type(dict_py))

# json.dumps把python数据类型转换为json字符串
# with open('shuju.json', 'w', encoding='utf-8') as f:
#     str_json = json.dumps(dict_py, ensure_ascii=False, indent=4)
#     print(str_json, type(str_json))  # str
#     f.write(str_json)

# 注: json字符串都是用双引号引起来的
# 具体read()或者write()方法的对象就类文件对象
# 如: f = open('xxx.txt','r') ---> f 就是类文件对象

# 使用json.load能够把文件对象中的数据提取出来转换为python类型
# with open('shuju.json', encoding='utf-8') as f:
#     rel = json.load(f)
#     print(rel, type(rel))  # dict

# 使用json.dump能够把python类型数据放入类文件对象中
# with open('shuju2.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_py, f, ensure_ascii=False, indent=4)
