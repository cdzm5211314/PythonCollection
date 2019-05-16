# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-05-16 16:06

import unittest

## unittest.TestCase中常用的断言方法:
# unittest.TestCase.assertEqual         # 如果两个值相等,则pass
# unittest.TestCase.assertNotEqual      # 如果两个值不相等,则pass
# unittest.TestCase.assertTrue          # 判断bool值为True,则pass
# unittest.TestCase.assertFalse         # 判断bool值为False,则pass
# unittest.TestCase.assertIn            # 在某个范围内,则pass
# unittest.TestCase.assertIsNone        # 不存在,则pass
# unittest.TestCase.assertIsNotNone     # 存在,则pass

# 定义一个类继承: unittest.TestCase
# 并定义两个固定方法: setUp(), tesrDown()
class TestClass(unittest.TestCase):
    """构造单元测试案例"""

    def setUp(self):  # 该方法会首先执行，相当于做测试前的准备工作
        pass

    def tesrDown(self):  # 该方法会在测试代码执行完后执行，相当于做测试后的扫尾工作
        pass

    def test_app_exists(self):  # 测试代码方法: 方法名以 test_开头
        pass



