# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

# 函数的练习:名片管理器

def displayMenu():
    print("-"*30)
    print("  名片管理系统    V8.8")
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.遍历查询所有名片")
    print("6.退出系统")
    print("-"*30)

# 用户的输入项信息
def getChoice():
    selectedKey = input("请输入序号...")
    return int(selectedKey)

# 遍历循环查看名片
def printAllinfo(list):
    for name in nameList:
        print(name)

# 定义一个变量保存名片
nameList = []

# 名片管理系统执行
while True:
    # 打印提示
    displayMenu()
    
    # 等待用户选择
    key = getChoice()
    if key == 1:
        print("    你选择了添加名片功能...")
        newName = input("请输入你的姓名")
        nameList.append(newName)
    elif key == 2:
        pass
    elif key == 3:
        pass
    elif key == 4:
        pass
    elif key == 5:
        printAllinfo(nameList)
    elif key == 6:
        break
    else:
        print("你输入有误,请重新输入...")
    
    
    
    
    
    
    
    
    
    