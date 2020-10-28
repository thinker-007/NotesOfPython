'''
面向对象最重要的概念是类（class）与实例(instance)
      #  class是抽象的概念，如human class,student class
      #  class中的函数称为class的方法
      #  instance是class创建出来的一个个具体的“对象”，每个对象拥有相同的方法(即类的方法)，但数据可能不同
'''
########################
'''
#  定义Class
'''
class Student(object):  #建立名为Student的class,object的所有class的base class
      school = "浠水第一中学"    #  class的初始属性
      math_teacher = "赵胜男"
'''
# 创建instance
'''
Milnor=Student() 
Milnor.height="178cm"  #  给instance绑定除基础属性之外的属性,身高
Milnor.weight="67kg"  
print("Milnor的学校：", Milnor.school)
print("Milnor的数学老师：", Milnor.math_teacher)
print("Milnor的身高：", Milnor.height)
###############################
'''
class的方法: 
      使用def关键字来定义一个方法.如下面的强制属性方法，__init__.
'''
'''
类属性
'''
class Student_sss(object):
      name = 'Student'   # 定义Student_sss class的属性
a=Student_sss()   # 那么a就有name为“Student"的属性
print(a.name)
'''
初始化: __init__, 创建具有强制属性的instance的方法
'''
class Human(object):
      def __init__(self, height, weight,birthday):  # self是实例变量
        self.height = height
        self.weight = weight
        self.birthday =birthday
Gauss=Human('178cm', "65kg", "1867-02-04")  # 调用时，实例变量self不必传入,这是必有属性
Gauss.title="伟大的数学家"    #  私有属性
print("Gauss的出生日期：", Gauss.birthday)


'''
instance的私有属性及其调用方法：
      #  第一种私有属性：属性名前加一个_: 外部可以直接访问
            ##  调用方法：实例名._属性名
      #  第二种私有属性：属性名前加两个__: 外部不可以直接访问
            ##  调用方法：实例名._类名__属性名
      #  dir()可以查看实例的所有属性和方法
'''
class People:
      name = "小明"
      _age = 13
      __sex = "male"
p=People()
print("年龄是：", p._age)
print("性别是：", p._People__sex)

'''
数据封装：
      #是面向对象编程的一个重要特点
      #将函数绑定到类中，称为类的方法
      #类的方法可以直接访问实例打数据，不需知道具体细节
'''
class Students(object):   #数据封装，get_score()在类里面定义
      def get_score(self):  # get_score()函数称为实例方法
            if self.score>90:
                  print("%s:A"% self.score)
            elif self.score>70:
                  print("%s:C"% self.score)
            elif self.score>50:
                  print("%s:D"% self.score)
Miss=Students()
Miss.score=78     
Meda=Students()
Meda.score=93
Nick=Students()
Nick.score=58
Miss.get_score()
Meda.get_score()



      