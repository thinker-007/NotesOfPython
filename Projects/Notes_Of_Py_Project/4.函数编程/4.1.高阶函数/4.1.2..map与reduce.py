#map()与reduce()是python内置函数

#map()
      ##map()接收两个参数，即map(函数名，可迭代对象)
x=map(abs,{-1,-4,6})
y=map(abs,[-1,-4,6])
print(x)   #map()输出的结果是一个迭代器Iterator
print(next(x))   #确实是迭代器
print(list(x))   #可用list将x中用list形式输出

#reduce()
      ##reduce()接收两个参数，把一个函数作用在一个序列上，即reduce(函数名，list,set or tuple or str)
from functools import reduce
def add(x,y):   #add()不是python内置函数,sum()是python内置函数
      return x+y
r=reduce(add,[1, 2, 3, 4])
r1=reduce(add,{1, 2, 3, 4})
print("r=",r)
print("r1=",r1)
print(sum([1,2,3,4]))

#例子：利用map()函数将用户输入的不规范的英文名改写成首字母大写