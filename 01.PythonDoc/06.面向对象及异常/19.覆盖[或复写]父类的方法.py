class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪叫...")

# XiaoTianQuan类拥有Dog类和Animal类的所有属性与方法
# 子类拥有父类以及父类的父类的所有属相和方法
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞起来..")

    # 覆盖父类的bark()方法
    def bark(self):
        print("我是神狗,吼吼叫...")


# 创建哮天犬对象
xiaotianquan = XiaoTianQuan()
# 如果子类重写了父类的方法时
# 在使用子类对象调用方法时,会调用子类重写的方法
xiaotianquan.bark()






