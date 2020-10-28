#filter()函数
      ##filter()是python内置的函数(BIF)，用于过滤序列。接收两个参数,filter(函数名, list,set or tuple or others)


#删除偶数
def is_odd(n):  #判断是否是奇数
      if n%2==1:
            return  n 
x=filter(is_odd, {2,4,5,7})  #filter()函数返回迭代器,选出奇数,对比下面的map有过滤的作用
print(next(x))
print(next(x))  #当然我们可以用list,set,tuple函数输出所有奇数
y=map(is_odd,{2,4,5,7})
print(list(y))   #输出为[None,None,5,7]


#用filter()函数求素数：埃氏筛法
def odd_num():  #创建从3开始的奇数列的generator
      n=1
      while True:
            n=n+2
            yield n
def not_divisible(n): #lambda表达式
      return lambda x:x%n >0  #若n整除x,那么输出True
def primes():    #输出大于等于二的素数的generator
      yield 2
      y=odd_num()  #初始序列
      while True:
            n=next(y)  #返回序列第一个数
            yield n
            y=filter(not_divisible(n),y)  #为什么not_divisible(n)是函数，参见下面的lambda表达式
p=primes()
n=1
while n<11:
      print(next(p))
      n=n+1


#例子：筛选回数

#lambda（闭包）表达式(匿名函数)
      ##lambda只是表达式，函数体比def简单很多
      ##lambda主体是一个表达式，而不是一个代码块（未缩进）
      ##起到一个函数速写的作用，允许在代码内嵌入一个函数的定义
f=lambda x,y,z: x+y+z  #对三个数求和,lambda更像一个映射
print(f(1,2,3))
g=lambda x:x%5>0
print(g(3))   #输出逻辑值True
# def not_divisible_s(n): #lambda表达式，筛选出不整除n的数
#       return lambda x:x%n >0  