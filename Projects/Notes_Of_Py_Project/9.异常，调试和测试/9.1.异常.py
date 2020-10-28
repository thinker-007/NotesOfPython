'''
python中标准异常：
      #  可以参考网站https://www.runoob.com/python/python-exceptions.html，我们选择几个见过的：BaseException---所有异常的基类，SyntaxError---语法错误，TypeError，ValueError---无效参数，UnicodeDecodeError---解码错误,FileNotFoundError
      #  异常exceptions:是一个python对象(BaseException的子类或实例)，表示一个错误
'''
########### 异常的处理之一：使用try...except...语句  ############################
'''
try语句形式 1：单个错误类型
      try：
            想要执行的代码块
      except <错误名称>:
            警告错误
      else:  #  可以省略else语句
            执行接下来的代码块  
'''
try:
      print(5/1)
except ZeroDivisionError:
      print("分母不能为零")  #  有错的话执行except语句
else:
      print("无错执行此句")   # 无措的话执行else语句，else部分可以省略

'''
try语句的形式 2：多种错误

      try:
            想要执行的代码块
      except(Exception1[, Exception2[,...ExceptionN]]]):
            发生上述多个错误中的一个执行此代码
      else:
            无措执行此代码
'''

'''
try语句的形式 3：任意错误

      try:
            想要执行的代码块
      except:  #  不输入错误类型
            发生错误执行此代码
      else:
            无措执行此代码
'''

############  异常的处理之二：使用try...finally...语句##############################
'''
try...finally...语句的作用：无论是否发生异常都将执行最后的代码

try...finally...语句的格式：
      try:
      <语句>
      finally:
      <语句>    #退出try时总会执行
'''
try:
      print(5/0)
finally:
      print("关闭文件")

