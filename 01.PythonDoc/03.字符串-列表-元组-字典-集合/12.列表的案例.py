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
print("输入5,退出系统...")
print("="*20)

stus = []
while True:
    temp = input("请输入你要的操作: ")
    if temp == "1":
        name = input("请输入你要添加的学生姓名: ")
        stus.append(name.strip(" "))
        print(stus)
    elif temp == "2":
        pass
    elif temp == "3":
        pass
    elif temp == "4":
        # print(stus)
        # name = input("请输入你要删除的学生姓名: ")
        # stus.remove(name.strip(" "))
        name = input("请输入你要删除的学生姓名: ")
        if name not in stus:
            print("你输入的学生%s不存在"%name)
            continue
        else:
            stus.remove(name)
        print(stus)
    elif temp == "5":
        break
    else:
        print("你输入有误,请重新输入...")