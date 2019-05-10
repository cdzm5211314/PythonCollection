# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2018-11-12 13:29

# __new__:创建对象时调用，会返回当前对象的一个实例
# __init__:创建完对象后调用，对当前对象的一些实例初始化，无返回值

# 继承自object的新式类才有__new__
# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
# __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
# 若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行


class Person():

    def __new__(cls, *args, **kwargs):
        print("new Person")
        return super().__new__(cls)

    def __init__(self):
        print("init ..")
        # return "Ok"  ## __init__ 无返回值

p = Person()
print(type(p))