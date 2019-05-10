# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

class Person:
    def __init__(self,name,weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重%.2f公斤" %(self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print("%s 爱跑步...,跑完步,体重会减少到%.2f" %(self.name,self.weight))

    def eat(self):
        self.weight += 1
        print("%s 爱吃东西...,吃完东西,体重会增加到%.2f"%(self.name,self.weight))


person1 = Person("小明",75.0)
print(person1)
person1.run()
person1.eat()
