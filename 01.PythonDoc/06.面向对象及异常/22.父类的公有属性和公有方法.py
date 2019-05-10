class A:

    def __init__(self):
        self.num1 = 100
        # 私有属性
        self.__num2 = 200

    # 私有方法
    def __test(self):
        print("num1的值为: %d,__num2的值为: %d"%(self.num1,self.__num2))

    # 公有方法
    def test(self):
        print("父类的公有方法...__num2 = %d"%self.__num2)
        self.__test()

class B(A):

    def demo(self):
        # 在子类的对象方法中不能访问父类的私有属性
        # print("在子类方法中访问父类的私有属性: __num2 = %d" %self.__num2)

        # 在子类对象的方法中不能调用父类的私有方法
        # self.__test()

        # 访问父类的公有属性
        print("在子类方法中访问父类的公有属性: %d" %self.num1)
        # 调用父类的公有方法
        self.test()

# 创建子类对象
b = B()
# 在外部直接访问父类的公有属性/调用公有方法
# 使用子类对象直接访问父类的公有属性:
print(b.num1)
b.test()

# 使用子类对象调用子类对象的方法访问父类的公有属性和方法
b.demo()



