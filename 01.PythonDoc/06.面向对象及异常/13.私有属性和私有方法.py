class Women:
    def __init__(self,name):
        self.name = name
        # 对象创建的时候就明确了年龄是多大
        # self.age = 18
        # 私有年龄age属性
        self.__age = 18

    def secret1(self):
        # 再对象的方法内部是可以访问对象的私有属性
        print("%s 的年龄是: %d"%(self.name,self.__age))
    # 私有方法
    def __secret2(self):
        # 再对象的方法内部是可以访问对象的私有属性
        print("%s 的年龄是: %d"%(self.name,self.__age))

# 创建一个Women对象
xiaohong = Women("小红")
# print(xiaohong.__age)  # 此行代码报错,私有属性不能再外部直接访问
xiaohong.secret1()

xiaohong.__secret2()  # 此行代码报错,私有方法不能再外部直接调用
