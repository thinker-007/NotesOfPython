'''
生成器
   #  class
   #  英文generator,一边循环一边计算的机制（算法），避免创建完整的list提高存储效率
'''

'''
创建生成器 generator V.S. 列表生成式
'''
'''方法一：将列表生成式的[]改成()'''
L=[x**2 for x in range(10)]
g=(x**2 for x in range(10))  #注意前面我们已讲没有tuple生成式
print(L)   #可以输出list L
print(g)   #输出generator,在需要时才输出结果，比输出整个列表省事
print("第一个=",next(g))  #输出第一个值0
print("第二个=",next(g))  #输出第二个值1
for a in g:     #接着上面输出g中的所有值4，...，81
      print(a)

'''方法二：使用yield 语句,创建generator function'''
#例子：斐波那契数列
def fib(n):  #斐波那契数列的第n项
      if n<=2:
            return 1
      while n>2:
            return fib(n-2)+fib(n-1)

def fib_output(n):  #输出斐波那契数列的前n项
      for i in range(n+1):
            print(fib(i))

def fib_former(n):
      a,b,s=0,0,1     #可以同时赋值
      while a<n:
            print(s)
            b,s=s,b+s
            n=n+1
      return "done"

def fib_generator():    #generator函数返回斐波那契数列
      a,s=1,1     #可以同时赋值
      while True:
            yield s   #替换print(s)
            a,s=s,a+s
def fib_generator_former(n):    #generator函数返回斐波那契数列的前n项的generator
      a,s=0,1      #可以同时赋值
      while n>=1:
            yield s   #替换print(s)
            a,s=s,a+s
            n=n-1
op=fib_generator_former(5)  #定义generator
print("斐波第一项=",next(op))

'''
将生成器转化成list,set,tuple输出
'''
print("op=",list(op))
print("op=",set(op))   #由于上面已经调用完数据，所以是空的
print("op=",tuple(op))


'''''''''
generator function 与普通函数的差异
      ##普通函数是顺序执行，遇到return语句或最后一行函数语句就返回
      ##generator function在每次调用next()函数时执行，遇到yield语句返回，再次执行从上次返回的yield语句处继续执行
      ##function调用一次返回一个（一组）值，而generator可以多次返回
      ##function可以被无数次重复调用，而一个generator实例在yield最后一个值 或者return之后就不能继续调用了
'''
def ord_s():
      print("step1")    #注意字符串要加单或双引号
      yield 1
      print("step2")
      yield(2)
      print("step3")
      yield(3)
o=ord_s()    #通过赋值变成generator
print(next(o)) #输出step1  1
print(next(o)) #输出step2  2   若没有赋值o=ord_s()，那么输出step1  1
print(next(o))      

#例子：杨辉三角
