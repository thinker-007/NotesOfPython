'''
collections模块：
      #  Python内建的一个集合模块，提供了许多有用的数据类型
      #  collections模块中常用的函数或类
            #  namedtuple: 具名元组或命名元组
            #  deque: 双向队列
            #  defaultdict
            #  OrderedDict
            #  Counter
      #  参考网站https://blog.csdn.net/abc_12366/article/details/80447228
'''
######################################################
'''
namedtuple:
      #  是一个函数，返回一个元组tuple的子类
      #  调用方式
      namedtuple("子类名", 元组字段名)
      子类名：名称的字符串
      元组字段名：字符串序列
            字符串组成的序列，如['x', 'y'], ('一之', '儿子')
            一个长字符串，各个字段名之间用空格或逗号分隔，如  x y   x,y
      #  它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
      #  可参考网站https://blog.csdn.net/jpch89/article/details/84645251
'''
from collections import namedtuple

Point = namedtuple("Point",['x_value', 'y_value'])  #  定义元组tuple的子类Point
first_point = Point(3,4)   #  定义点的实例
x_first_point = first_point.x_value  #  用属性调用点的元素
y_first_point = first_point[1]  #因为Point类是tuple的子类，那么也可以实用索引的方法调用元素
print(x_first_point)
print(y_first_point)

print(isinstance(first_point, tuple))
#  定义Circle类，[圆心坐标，半径]
Circle = namedtuple('Circle', 'x, y, r')
c1 = Circle(2,3,5)  #   定义了一个园的实例

###################################################
'''
deque: double-ended queue
      #  是一个类，
      #  在 list 的基础上增加了移动、旋转和增删方法：
            append():在尾部添加元素，list 方法
            pop()：取出尾部元素，list 方法
            extend(): 在尾部添加多个元素
            appendleft(): 在头部添加元素
            popleft(): 取出头部元素
            count():计算队列中元素频次
      #  参考网站https://blog.csdn.net/HappyRocking/article/details/80058623
'''
from collections import deque
q = deque(['一之', '九之', '吊儿'])  #  定义deque的一个实例
x = q[2]
y = q.pop()  #  取出最右边的元素, 队列q将减去此元素
z = q.popleft()
w = q.count('一之')
print(x,'\n',y, '\n', z, '\n', w)  # 显示一之被取出
print(isinstance(q, list))  #  q并不是list类的实例

###########################################################
'''
defaultdict:
      #  function_factory: 工厂函数
      #  工厂函数：在这基础之上， 原来的所谓内建转换函数像int(), type(), list() 等等， 现在都成了工厂函数。 也就是说虽然它们看上去有点象函数， 实质上他们是类。当你调用它们时， 实际上是生成了该类型的一个实例， 就像工厂生产货物一样。
      #  VS dictionary:除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的 
'''
from collections import defaultdict

d = defaultdict(lambda: 'expression')
print(d['key1'])  #  没有key值，输出默认值'expression'

##############################################################
'''
OrderedDict:
      #  作用：使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict。
      #  可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
'''
dict1 = dict([('a',1), ('b',2), ('c',3)])
print(dict1.keys())
print(dict1)  #  可能无序

from collections import OrderedDict

dict2 = OrderedDict([('a',1), ('b',2), ('c',3)])
print(dict2)

########################################################
'''
ChainMap:
      #  是一个class
      #  可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找
      #  参考网站https://blog.csdn.net/langb2014/article/details/100122209
'''

###########################################################
'''
Counter:
      #  是dict的一个子类
      #  统计字符出现的个数
      #  参考网站https://blog.csdn.net/qwe1257/article/details/83272340
'''
from collections import Counter

c = Counter()  #  创建一个空的Counter实例

