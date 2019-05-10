# Python3.x 默认都是新式类,经典类被废除,不必显示的继承object
# Python2.x 默认都是经典类,只有显示的继承了object,才是新式类

# 注意:为了保证编写代码能在同时在Python2.x和Python3.x上运行!!!
# 在定义类时,如果没有父类,建议统一继承自object
class 类名(object):
    pass

### 继承后方法的调用顺序(广度优先与深度优先)
# 新式类: 广度优先  BB ---> CC --->AA
# 经典类: 深度优先  BB ---> AA ---> CC

class AA():
    pass
class BB(AA):
    pass
class CC(AA):
    pass
class DD(BB,CC):
    pass



