'''
参考网站https://www.liujiangblog.com/course/python/43
'''

'''
枚举类的由来：
      #  枚举类型可以看作是一种标签或是一系列常量的集合，通常用于表示某些特定的有限集合，例如星期、月份、状态等
      #  特点：不能被篡改
'''

'''非枚举类的处理方法'''
Color = {"red": 1, "green": 2, "blue": 3}   # dict的形式
class Colors:      # 默认为最大class object的子类，可以省略
      red = 1
      green = 2
      blue = 3
Colors.red = 9
print("red", Colors.red)   # red 值被篡改

'''使用枚举类的方法: Enum 类型'''
from enum import Enum
class Colors_s(Enum):   # 在class Enum下建立subclass Colors_s
      yellow = 4
      black = 5
      white = 6
'''
Colors_s.yellow = 8
print("黄色",Colors_s.yellow)  #  显示不能篡改
'''
###########################################

'''
定义枚举：
      #  定义枚举时，属性名不允许相同
'''
class Colors_ss(Enum):   # 在class Enum下建立subclass Colors_s
      yellow = 1
      black = 5
      yellow = 2    # 错误，不允许有两个相同属性 yellow
      #  成员值允许相同，相同中的第二个成员的名称被视作第一个成员的别名'''
class Color_ss(Enum):
    red   = 1
    green = 2
    blue  = 1
print(Color_ss.red is Color_ss.blue)
'''若要不能定义相同的成员值，可以通过 unique 装饰
from enum import Enum, unique
@unique
class Color_sss(Enum):
    red   = 1
    green = 2
    blue  = 1   #  显示错误，重了
'''
#############################################

'''
枚举取值
      #  可以通过成员名来获取成员也可以通过成员值来获取成员
'''
print(Color_ss['red'])  # Color.red  通过成员名来获取成员

print(Color_ss(1)) 


'''''''''''练习题''''''''''''''''''
把Student的gender属性改造为枚举类型，可以避免使用字符串'''


