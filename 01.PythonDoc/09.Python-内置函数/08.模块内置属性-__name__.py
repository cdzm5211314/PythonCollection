# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-03-18 10:54

import 模块内置属性__file__

# 在导入文件时,所有没有任何缩进的代码都会执行一遍

# __name__ 属性可以做到 测试模块代码 只在测试的情况下运行, 而在被导入时不被执行

# 如果是 被其他文件导入的, __name__的值就是 导入的模块名
# 如果是 当前执行的程序,__name__的值就是 __main__
# 注: 执行当前模块时,__name__的值永远都是__main__

# 注意: 模块中直接执行的代码不是向外界提供的工具

if __name__ == "__main__":
    print(__name__)

# ***********************************************************
# 在导入文件时, 文件中 所有没有任何缩进的代码 都会执行一遍

# 实际开发中,当前模块的测试代码 只在测试的情况下执行,而在被导入其他文件时,不被执行!!! __name__ 属性可以做到
# __name__ 是Python 解释器内置属性,记录着一个字符串
# 如果 是被其他文件导入的, __name__ 就是模块名
# 如果 是当前执行的程序, __name__ 就是 __main__

# 在代码的最下方
def main():
    # 需要测试的代码
    pass

# 根据 __name__ 属性判断是否执行下方的代码
if __name__ == "__main__":
    main()

def test():
    print("-----test-----")
print(__name__)

# __name__这个变量,是在python执行的时候有一个默认的值
# 1.如果python3 aaa.py 那么此时__name__这个变量的值为 __main__
# 2.如果在bbb.py文件中,去import aaa.py文件的话,那么此时这个__name__的值为 import文件的名字aaa
# 例如:python3 aaa.py ---> __name__ = __main__
#      python3 bbb.py ---> aaa.py文件的 __name__ = aaa
#                          bbb.py文件的 __name__ = __main__
