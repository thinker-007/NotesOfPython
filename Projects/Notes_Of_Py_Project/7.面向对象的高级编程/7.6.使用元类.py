'''
type()的两种用途:
      
'''
'''
一个参数的情况：判断数据类型
      #  基本语法：type(object)
'''
print(type(1))  #  显示1是int类型
print(type("张一之"))  #  显示“张一之”是str类型

'''
三个参数的情形：返回一个class对象
      #  基本语法：type(class_name, base classes, dict)  dict: 类的属性方法和值组成的键值对
'''
#  用type()生成上面的一个class A
A = type("A", (), {"name": "张九之"}) 

#  还可以创建A的subclass B
B = type("B", (A,), {"age": 15})   #  加上了私有属性
python = B()
print("B的名字：", python.name)
print("B的年龄：", python.age)
#############################################
'''
type() VS isinstance()
      #  type不会认为子类是父类的类型，不会考虑继承关系
      #  isinstance会任务子类是父类的类型，考虑继承关系
'''
print(isinstance(python, A))  # True
print(type(python) == A)     #  False
print(type(python) == B)     #  True
      
'''
元类：metaclass
'''