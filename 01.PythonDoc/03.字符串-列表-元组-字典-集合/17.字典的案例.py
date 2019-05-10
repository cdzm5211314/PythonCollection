# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

print("="*20)
print("学生的管理系统:".center(12))
print("输入1,表示添加学生")
print("输入2,查找学生姓名")
print("输入3,修改学生姓名")
print("输入4,表示删除学生")
print("输入5,查看所有学生")
print("输入6,退出系统...")
print("="*20)
# 学生列表中包含了很多学生的信息
stus = []
while True:
    temp = input("请输入你要的操作: ")
    stu = {}
    if temp == "1":
        name = input("请输入你要添加的学生姓名: ")
        age = int(input("请输入你要添加的学生年龄: "))
        phone = int(input("请输入你要添加的学生手机: "))
        # 定义一个字典存储一个学生的信息,一个学生包含姓名,年龄,手机号
        stu["name"] = name
        stu["age"] = age
        stu["phone"] = phone
        stus.append(stu)
        print(stus)
    elif temp == "2":
        name = input("请输入你要查找的学生姓名")
        for item in stus:
            if item["name"] == name.strip():
                print("你查找的学生姓名为:%s ,年龄:%d ,手机号:%d "%(item["name"],item["age"],item["phone"]))
                break
            else:
                print("你所有查找的学生%s不存在..." % name)
    elif temp == "3":
        pass
    elif temp == "4":
        pass
    elif temp == "5":
        print("序号\t姓名\t年龄\t手机")
        for i,item in enumerate(stus,1):
            print("%d\t%s\t%d\t%d"%(i,item["name"],item["age"],item["phone"]))
    elif temp == "6":
        break
    else:
        print("你输入有误,请重新输入...")


