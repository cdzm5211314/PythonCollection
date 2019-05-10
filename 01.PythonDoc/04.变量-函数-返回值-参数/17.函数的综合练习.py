# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 综合练习：学生管理系统

def showInfo():
    print("-"*30)
    print("    学生管理系统    v1.0")
    print(" 1:添加学生信息")
    print(" 2:删除学生信息")
    print(" 3:修改学生信息")
    print(" 4:查询学生信息")
    print(" 5:遍历所有学生信息")
    print(" 6:退出系统")
    print("-"*30)
    
# 定义一个全局变量用来存储添加的学生信息
students = []

# 添加学生功能
def add(students):
    name = input("学生的姓名:")
    age = int(input("学生的年龄:"))
    stuId = int(input("学生的学号:"))
    # 定义一个字典用来保存学生的信息
    stuInfo = {}
    stuInfo["name"] = name
    stuInfo["age"] = age
    stuInfo["id"] = stuId
    students.append(stuInfo)

# 删除学生功能
def delete(students):
    # 根据列表的下标删除元素
    delNum = int(input("请输入你要删除的序号:"))
    del students[delNum]
  
# 学生管理系统
while True:
    # 1.0 先把功能列表进行显示
    showInfo()
    # 1.1 提示用户选择功能
    # 1.2 获取用户选择的功能
    key = int(input("请选择功能(序号):"))
    
    # 1.3 根据用户的选择，执行相应的功能
    if key == 1:
        # 完成学生的添加功能
        add(students)
    elif key == 2:
        delete(students)   
    elif key == 3:
        pass  
    elif key == 4:
        pass
    elif key == 5:
        print("遍历所有的学生信息...") 
        print("学号       姓名       年龄") 
        for temp in students:
            print("%d     %s   %d"%(temp.get("id"),temp.get("name"),temp.get("age")))
    elif key == 6:
        quitConfirm = input("亲,你真的要退出么(yes or no)???")
        if quitConfirm == "yes":
            break  
    else:
        print("你输入有误,请重新输入...")










