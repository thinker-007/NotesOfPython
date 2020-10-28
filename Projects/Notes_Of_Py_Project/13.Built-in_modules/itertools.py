'''
itertools:
      #  BuILt-in module
      #  itertools就是用来操作迭代器的一个模块，包含的函数都是能够创建迭代器来用于for循环或者next().
      #  主要三类函数：无限迭代器，有限迭代器，组合迭代器
      #  参考网站https://www.jianshu.com/p/34de5245aca5
'''
######################################
'''
无限迭代器： infinite iterators
      #  count()函数： 格式count([迭代初始值], [步数])迭代初始值默认为0，步数默认为1
      #  cycle()函数:  格式cycle(可迭代对象)把传入的一个序列无限重复下去
      #  repeat()函数： 格式repeat(element, [重复次数])方括号表示有默认值，默认值为无限
'''
from itertools import *  #  不能直接import itertools

counter = count(4, 2)  # 定义了一个初值为4迭代步数为2的无限序列
print(next(counter))

cycles = cycle('123')   #  形成一个长的字符串
i = 0
for x in cycles:
      i =  i+1
      print(x)
      if i>5:
            break

repeats = repeat('123')   #  重复字符串，注意与cycle的差异
j = 0
for x in repeats:
      j =  j+1
      print(x)
      if j>5:
            break

repeats_s = repeat('abc', 3)  #  重复指定的次数
for x in repeats_s:  #  上述是迭代器，输出对象的方法
      print(x)
#########################################
'''
有限迭代器：iterators terminating on the shortest input sequence
      #  chain(): 可以把多个可迭代对象组合起来，形成一个更大的迭代器
      #  groupby(): 把迭代器中相邻的重复元素挑出来放在一起
      #  accumulate(): 可以计算出一个迭代器。格式
            accumulate(iterable, [func]) 默认值为加法
'''
combi = chain("abc", "ABC")
for x in combi:
      print(x)

abc = groupby('abbbcccaaa')
for x in abc:
      print(x)

sum_seq = accumulate([1,2,6,7,4,8])  # 默认求迭代和
for x in sum_seq:
      print(x)

max_seq = accumulate([1,2,6,7,4,8], max)
for x in max_seq:
      print(x)

################################################
'''
组合迭代器：combinatorical iterators
      #  组合操作包括排列，笛卡儿积，或者一些离散元素的选择，组合迭代器就是产生这样序列的迭代器
      #  product()函数：
      #  permutations()函数：
      #  combinations()函数：
'''