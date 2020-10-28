#高阶函数
      ##即higher-order function,把函数作为参数传入，这样的函数称为高阶函数

#变量可以指向函数
f=abs   #函数赋值时，只需写函数名，不能写成f=abs()
print(f(-1))

#函数名也是变量
abs=10
print(abs)
# print(abs(-1))  #绝对值函数失效

#传入函数
def m(x,y,z):   #定义一个简单的高阶函数
      return z(x)+z(y)
print(m({-1,2},{6,7},max))