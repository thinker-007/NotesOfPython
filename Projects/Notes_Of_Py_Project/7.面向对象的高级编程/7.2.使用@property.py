'''
@property装饰器：
      #  python内置装饰器，用于把class中的一个方法(class中的函数)变成attribute(属性)
      #  可以参考网页https://blog.csdn.net/jpch89/article/details/84026130?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
'''
#########################
'''
property应用场景：
      #  在get,set,delete对象属性的时候，需要额外做一些工作。比如在游戏编程中，设置敌人死亡之后需要播放死亡画面。
      #  需要限制对象属性的设置和获取(只读，只写). 如用户数据为只读，或者在设置用户年龄时有范围限制。
      #  上述情形下就用到property工具，他把方法包装成属性，让方法可以以属性的形式被访问和调用
'''
################################
'''
property()函数：python内置函数(built-in function)  检查help(property)
   property(fget=None, fset=None, fdel=None, doc=None)
   #  fget：get属性值的方法
   #  fset: set属性值的方法
   #  fdel: delete属性值的方法
   #  doc:  属性描述信息，如果省略，会把fget方法的docstring(文档字符串)拿来用（如果有的话）
'''
class Student(object):
      def __init__(self):    #  实例属性的初始化
            self._age=None
      def  get_age(self):
            print("get属性时的代码")
            return self._age
      def set_age(self,new_age):    #   设置新年龄
            print("set属性时的代码")
            self._age=new_age
      def del_age(self):
            print("delete属性时的代码")
            del self._age   
Gauss = Student()   
print(Gauss._age)   
Gauss.set_age(17)   # set 新的age为17
print(Gauss.get_age())  #  得到的新的年龄,注意调用方法的方式

'''我们把上面的过程用property()函数写的更简单一些'''
class Students(object):
      def __init__(self):
            self._age=None
      def  get_age(self):
            return self._age
      def set_age(self,new_age):   
            self._age=new_age
      def del_age(self):
            del self._age     
      age = property(get_age, set_age, del_age)  # 省去get，set等
Euler = Students()  #  实际调用get_age,对比上面的命令行
print("欧拉的默认年龄：",Euler.age)
Euler.age = 18   # 定义欧拉的新年龄,实际调用方法set_age
print("欧拉的准确年龄：", Euler.age)

'''
用装饰器@property让上述过程更简洁
'''
class Students_s(object):  
      def __init__(self):
            self._age=None
      
      @property
      def  age(self):       #  get的age
            return self._age
      
      @age.setter
      def age(self,new_age):    #  设置新年龄
            self._age=new_age
Riemann = Students_s()
print("黎曼的初始年龄：",Riemann.age)
Riemann.age = 19
print("黎曼的准确年龄：", Riemann.age)
#############################################
'''
只读与只写
'''
class Students_ss(object):  
      def __init__(self):
            self._age=None
      
      @property
      def  age(self):       #  get的age
            return self._age
      
      @age.setter
      def age(self,new_age):    #  设置新年龄
            self._age=new_age
      
      @property               # 虚岁nominal age是只读
      def nominal_age(self):
            return self._age-1
Cartan = Students_ss()
Cartan.age=101
print("嘉当的虚岁：",Cartan.nominal_age)

'''
Exercise: 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution.
'''