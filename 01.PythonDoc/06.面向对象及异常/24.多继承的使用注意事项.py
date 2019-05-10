class A:
    def test(self):
        print("A类 test 方法...")
    def demo(self):
        print("A类 demo 方法...")
class B:
    def test(self):
        print("B类 test ...方法")
    def demo(self):
        print("B类 demo 方法...")

# 多继承可以让子类对象同时具有多个父类的属性和方法
# 在开发中如果多个父类中存在同名的属性或方法时,尽量避免使用多继承
class C(A,B):
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

# 以上结果显示如下,A与B有同名的,调用的时候谁先继承就调用谁
# A类 test 方法...
# A类 demo 方法...

# 确定C类对象调用方法的顺序
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
