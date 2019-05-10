class A:

    def __init__(self):
        self.num1 = 100
        # 私有属性
        self.__num2 = 200

    # 私有方法
    def __test(self):
        print("num1的值为: %d,__num2的值为: %d"%(self.num1,self.__num2))

class B(A):

    def demo(self):
        # 在子类的对象方法中不能访问父类的私有属性
        # print("访问父类的私有属性: __num2 = %d" %self.__num2)

        # 在子类对象的方法中不能调用父类的私有方法
        # self.__test()
        pass


# 创建子类对象
b = B()
print(b.num1)
b.demo()
# print(b.__num2)  # 在外部不能直接访问父类或对象本身的私有属性
# b.__test()  # 在外部不能直接调用父类或对象本身的私有方法






