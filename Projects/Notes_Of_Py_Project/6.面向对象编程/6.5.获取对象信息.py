'''
对象的类型判断：type()
'''
type(123)   # 可以查出123数int class中的instance,即123是整数型数据
print(type("张耀华"))  # 输出 str，即"张耀华"是str class中的instance,也就是字符串

class Animal(object):  
      pass
dog=Animal() 
print(type(dog))    # 输出<class '__main__.Animal'>
#####################################
'''
判断class的类型：isinstance()
'''
isinstance({1,2,3},(list,tuple))  # 判断{1，2，3}是list类型或者是tuple类型
#############################
'''
获得对象的所有属性和方法：dir()
'''
print(dir("赵胜男"))  
print(dir(dog))