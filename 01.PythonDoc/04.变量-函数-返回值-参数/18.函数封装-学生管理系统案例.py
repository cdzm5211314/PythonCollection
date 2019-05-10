# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 打印菜单的函数
def print_menu():
    print("="*20)
    print("学生的管理系统:".center(12))
    print("输入1,表示添加学生")
    print("输入2,查找学生姓名")
    print("输入3,修改学生姓名")
    print("输入4,表示删除学生")
    print("输入5,查看所有学生")
    print("输入6,退出系统...")
    print("="*20)
# 添加学生的函数
def add_student():
    name = input("请输入你要添加的学生姓名: ")
    age = int(input("请输入你要添加的学生年龄: "))
    phone = int(input("请输入你要添加的学生手机: "))
    # 定义一个字典存储一个学生的信息,一个学生包含姓名,年龄,手机号
    stu = {}
    stu["name"] = name
    stu["age"] = age
    stu["phone"] = phone
    stus.append(stu)
    print(stus)
# 查找学生的函数
def search_student(name):
    for item in stus:
        if item["name"] == name.strip():
            print("你查找的学生%s存在..."%name)
            print_student(item)
            break
    else:
        print("你所有查找的学生%s不存在..." % name)
# 打印学生的信息
def print_student(item):
    print("%s\t%d\t%d" %(item["name"], item["age"], item["phone"]))
# 打印所有学生信息
def print_all_student():
    print("序号\t姓名\t年龄\t手机")
    for i, item in enumerate(stus, 1):
        print("%d\t"%i,end="")
        print_student(item)
# 主函数
def main():
    print_menu()
    while True:
        temp = input("请输入你要的操作: ")
        if temp == "1":
            add_student()
        elif temp == "2":
            name = input("请输入你要查找的学生姓名")
            search_student(name)
        elif temp == "3":
            pass
        elif temp == "4":
            pass
        elif temp == "5":
            print_all_student()
        elif temp == "6":
            break
        else:
            print("你输入有误,请重新输入...")

# 全局变量:学生列表中包含了很多学生的信息
stus = []

# 调用函数执行程序
main()