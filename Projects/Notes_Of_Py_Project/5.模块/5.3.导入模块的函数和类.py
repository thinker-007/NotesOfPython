'''
导入模块的函数和类：
      #  导入模块的函数参考网页https://blog.csdn.net/Mr_Cat123/article/details/80515370
      #  导入模块的类参见网页https://blog.csdn.net/toby54king/article/details/89851808
'''
###########################

'''
导入模块的函数：
'''
import text2.fibo2
text2.fibo2.fib(5)
'''fib(5)   调用错误'''
from text2.fibo2 import fib
fib(5)
#############################

'''
导入模块中的一个类
'''
from text2.run import Person as P     #  一个简写的办法
p = P()   #  定义一个Person的实例，自动拥有初始属性
p.name()      # name是函数，()不能省
p.age()
####################################
'''
导入模块中的多个类
'''
from  text2.run import Person, Woman, Man
w = Woman()
w.sex()
######################################
'''
导入模块中的所有类
'''
from text2.run import*
m = Man()
m.sex()