class Women:
    def __init__(self,name):
        self.name = name
        # 私有年龄age属性
        self.__age = 18

    # 私有方法
    def __secret2(self):
        # 再对象的方法内部是可以访问对象的私有属性
        print("%s 的年龄是: %d"%(self.name,self.__age))

# 创建一个Women对象
xiaohua = Women("小花")
# 访问私有的属性:不建议使用
print(xiaohua._Women__age)
# 访问私有的方法:不建议使用
xiaohua._Women__secret2()

