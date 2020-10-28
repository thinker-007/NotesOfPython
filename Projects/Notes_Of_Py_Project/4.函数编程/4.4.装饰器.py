'''
装饰器（decorator）
      #  本质上是一个python函数或类，是一个返回函数或类的高阶函数(以函数作为变量之一)
      #  作用：它可以让其它函数或类在不需要做任何代码修改的情况下，给函数增加额外的功能。
      #  在装饰器里，只有”return 变量“时才执行被装饰的函数
      #  应用场景：插入日志，性能测试，事务处理，缓存，权限校验等场景
'''
################################
'''
函数的包装：func()————>包装后的func()  
'''
def ahead_decorator(func): 
      print("Hello")
      return func
def wrapper():    # 不出现在代码中可以空着
      print("world")
wrapper = ahead_decorator(wrapper)  #  输出包装后的terget函数

'''
包装的简单写法：@语法
'''
@ahead_decorator #装饰器，return fun 语句执行被装饰函数target_s，所以输出Hello world
def terget_s():
      print("world")
terget_s()

#例子：
def decorator_s(x):    #定义装饰器
      print("下面是一个加法函数",end='')   #这里end=可以输出return值
      return x
@decorator_s
def sum(x,y):
      return x+y
print(sum(1,2))

#装饰器调用被装饰函数
def decorator_sss(x):     #定义装饰函数
      def star(a,b):
            ab=a*b
            print("*"*ab)   #可以调整位置
            x(a,b)        #相当于此处用x表示sum_s函数          
      return star         #这里返回star函数
@decorator_sss
def sum_s(a,b):
      s=a+b
      print(s)
sum_s(1,5)

def decorator_star(x,y):  #输出一个函数
      xy=x*y
      print("*"*xy)
      def wrapper(func):   #wrapper即包装
            return  func
      return wrapper
@decorator_star(2,5)
def sum_ss(a,b):
      s=a+b
      print(s)
sum_ss(1,4)

#例子：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

#例子：编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志