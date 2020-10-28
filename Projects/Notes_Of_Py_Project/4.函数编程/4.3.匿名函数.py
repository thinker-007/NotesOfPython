''' 匿名函数，lambda函数表达式 '''
      ##是一个函数对象，可以赋值给一个变量
f=lambda x,y,z: x+y+z  #对三个数求和,lambda更像一个映射
print(f(1,2,3))
g=lambda x:x%5>0
print(g(3))  

#匿名函数作为返回值
def sum(x,y):    #不是闭包，nested function没有调用outer enclosing function 的变量
      return lambda x,y: x+y  #返回函数,并未调用非本地变量(x,y)
z=sum(1,2)   #不论(n,m)怎么取值，都输出lambda表达式，或者说函数(x,y)->x+y
w=sum(7,8)
print("z=",z(2,2))
print("w=",w(2,2))
def sum_s(n,m):  #是闭包
      return lambda: n+m  #调用outer enclosing function的变量的方式,注意冒号
r=sum_s(1,2)  #r是无变量函数，取值3
print("r=",r())

#例子：用匿名函数改造下面的代码
def is_odd(n):   #奇数判断
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))  #过滤出奇数
print(L)