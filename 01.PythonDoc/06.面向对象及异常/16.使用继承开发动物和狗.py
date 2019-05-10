class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

# 子类拥有父类的所有属性和方法
# 子类可以封装自己特有的属性和方法
class Dog(Animal):
    def bark(self):
        print("汪汪叫...")

# 创建狗对象
# wangcai = Animal()
wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()


