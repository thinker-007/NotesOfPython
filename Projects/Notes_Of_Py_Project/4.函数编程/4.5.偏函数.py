#偏函数（partial function）
      ##functools模块中的函数，
      #3调用格式：functools.partial(函数对象，参数设置)
      ##作用：固定函数的参数，形成新函数

#整数的进制转换
      ##int()函数默认转换成十进制整数，即int(number,base=10)
import functools

int17=functools.partial(int,base=17)   #将17进制数换算成10进制
print(int17("18"))   #输出25
print(int17("18",base=15))  #重新修改int17的参数将15进制数18输出为十进制，结果为23

max2=functools.partial(max,10)
print(max2(35,7,9,12))