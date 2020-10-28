'''
dir()函数：
      #  作用：查看对象内的所有的属性和方法。
      #  dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表
      #  带参数时，返回参数的属性、方法列表。
      #  参考网站https://blog.csdn.net/sunxiaopengsun/article/details/104568935
'''
print(dir())
print(dir([]))   # 查看list类中的方法，变量等
import collections
print(dir(collections))  #  查看collections模块中的类，方法，变量等