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

    # 覆盖父类的bark()方法,并对
    def bark(self):
        # 子类特有的需求,编些代码
        print("我是神狗,吼吼叫...")
        # 使用super().调用原本在父类中封装的代码
        super().bark()
        # 使用父类名.方法(self)调用父类的方法--->不建议使用
        # Dog.bark(self)
        # 也可以再增加其他代码

# 创建哮天犬对象
xiaotianquan = XiaoTianQuan()

xiaotianquan.bark()






