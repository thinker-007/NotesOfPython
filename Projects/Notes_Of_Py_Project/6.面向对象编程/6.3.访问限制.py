'''
篡改instance的属性
'''
class Students(object):   #数据封装，get_score()在类里面定义
      def __init__(self,name,score):  #  初始化属性
            self.name=name
            self.score=score
张三=Students("Miss",79)  #变量名不能用单双引号的字符串，不能写成“张三” 
print(张三.name)

张三.name="Kobe" #赋值右边必须是一个数据，整数，浮点数，字符串，dict等，不能数Kobe(变量写法)
print(张三.name)   #篡改了class的内部属性

'''
访问限制：private 变量
      实例的变量名前加_变成private 变量
'''
class Students_s(object):   #数据封装，get_score()在类里面定义
      def __init__(self,name,score):
            self.__name=name    #取name的变量名为self.__name
            self.__score=score
张三=Students_s("Miss",79) 
'''
print(张三.name)   #无法访问
print(张三.__name)
'''

'''
外部获取属性的方法：
'''
class Students_ss(object):   #数据封装，get_score()在类里面定义
      def __init__(self,name,score):
            self.__name=name    #取name的变量名为self.__name
            self.__score=score
      def get_name(self):   #获取name
            return self.__name
张三=Students_ss("Miss",79) 
print(张三.get_name())
'''
print(张三.__name)  #私有变量，外部不能访问
'''

'''
练习题:
'''
