'''
测试函数的方法：单元测试和测试用例
      #  单元测试：unittest
'''
#################################
'''
测试函数：
'''
# 定义合成姓名的函数,见文件name_function.py
from name_function import get_formatted_name
new_name = get_formatted_name('Jim', 'Boss')
print(new_name)

#  我们设计一个测试的程序，即当输入first与last name时，输出希望的那样
first = input("first name:")
last = input("last name")
full_name = get_formatted_name(first, last)
print("你的全名是：", full_name)

###################################
'''
单元测试和测试用例：
      #  单元测试unittest：是python内置模块，用于核实函数的某个方面没有问题
      #  测试用例：一组单元测试，
      #  全覆盖测试用例：
      #  unittest.TestCase是模块unittest中的class
'''
import unittest

class NameTestcase(unittest.TestCase): 
 #  unittest.TestCase是unittest中的类，为什么在导入的时候不提及了
      def test_first_last_name(self):
            full_name = get_formatted_name('Jim', "Boss")
            self.assertEqual(full_name, 'Jim Boss')   
            #  使用unittest.TestCase中的方法assertEqual

unittest.main()  #  显示OK

