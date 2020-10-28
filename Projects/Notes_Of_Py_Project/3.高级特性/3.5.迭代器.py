'''
迭代器：Iterator
      #  class
      #  可以被next()函数调用并不断返回下一个值的对象
'''
'''Iterator（迭代器）的判断,区别于Iterable对象'''
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
#  list,dict,str不是迭代器

'''
可迭代对象：Iterable, class
      #  for循环作用的数据对象统称为可迭代对象，即Iterable,如集合数据类型：list，tuple，dict,set,str(字符串)等
      #  一类是generator，包括生成器和带yield的generator functions
'''
'''Iterable对象的判断'''
from collections.abc import Iterable
print(isinstance([], Iterable))

'''
生成器VS迭代器
      ##生成器都是迭代器，因为next()函数可以作用generator
      ##？？
'''

'''
将可迭代对象（Iterable对象）转化成迭代器（Iterator对象）的方法：
'''
for x in "abc":  #字符串是可迭代对象即Iterable对象
      print(x)
x="abc"
# print(next(x))  #显示错误，字符串不是迭代器
y=iter('abcd')  #将字符串变成迭代器
print(next(y))   #输出a
print(next(y))   #输出b

'''
将迭代器转化成list,set,tuple输出
'''
print(list(y))   #输出list["c","d"]