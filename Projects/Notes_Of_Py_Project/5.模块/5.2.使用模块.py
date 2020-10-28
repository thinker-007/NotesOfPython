'''
模块的导入：两种基本方法
      #  import:
                  import package_name1.package2_name ... module_name
      #  from ... import ...
                  from 包名1.报名2. ...  import module_name
                  from 包名1.包名2...模块名 import 变量名/函数名/类
      #  不同的导入方法，调用方法或函数的操作不一样'''
      

##################################
'''
导入内置模块
      #  关于built-in module可参考网址https://blog.csdn.net/xmm1981/article/details/79170126'''
import pydoc

#################################
'''
导入同目录的模块: 使用上述方法

'''
import fibo   #模块python语句（第一行）执行，输出_name_:fibo，函数并未执行
fibo.fib(5)   #调用模块fibo中的函数格式

from fibo import fib
fib(5)
#####################################
'''
导入不同目录的模块
      #  任意目录的情形参考网页https://blog.csdn.net/Mr_Cat123/article/details/80515370
'''
from text2.fibo2 import fib   #  注意让text2包与当前文件处于同一目录
fib(5)

import  text2.fibo2
text2.fibo2.fib(5)


