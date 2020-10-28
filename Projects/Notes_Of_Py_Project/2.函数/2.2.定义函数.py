#内置函数与自定义函数

#定义函数
      ##定义函数要用def语句,依次写出函数名、括号、括号中的参数、冒号，然后缩进块编写函数体,函数值用return语句返回
      ##my_abs函数的定义
def my_abs(x):
      if x>=0:
            return x    #函数体内部语句执行到return语句函数就执行完毕并返回结果
      else:
            return -x
print(my_abs(-1))
      ##调用上述文件在后面模块讨论

#空函数
def kong():
      pass   #pass语句什么都不做，占位且使函数结构完整，待后面再来完善

'''
参数检查
      ##对于自定义的函数，为了避免输入错误的数据类型，可以用内置函数来参数检查，配合raise语句
def my__abs(x):
      if not isinstance(x,(int,float)):
            raise TypeError("不是正确类型")
      if x>=0:
            return x    
      else:
            return -x
print(my__abs("张耀华"))   #输出判断结果，不是正确类型
'''

#返回多个值
import math    #导入math包，允许后续代码调用math中的函数
r=math.sin(math.pi/2)  #调用math包函数的方式
print("r=",r)
q=math.e   
print("%.3f"% q)     #输出e的三位小数
print(format(q,".3f"))  #使用formate函数输出e的三位小数
print('{name}在{option}'.format(name="张某人",option="写代码"))  #对字符串的操作
print('{1}在{0}'.format('张耀华','写代码'))  #0，1决定了顺序，输出写代码张耀华

#一元二次函数的解
def quadratic(a,b,c):
      deta=b**2-4*a*c
      if deta<0:
            print("此方程无解")
      elif deta==0:
            x=(-b)/(2*a)
            print("此方程有为一解%s"%x)
      else:
            x1=(-b-math.sqrt(deta))/(2*a)
            x2=(-b+math.sqrt(deta))/(2*a)
            print("此方程有两个解x1=%s和x2=%s"%(x1,x2))
print(quadratic(1,2,3))
print(quadratic(3,4,1))
