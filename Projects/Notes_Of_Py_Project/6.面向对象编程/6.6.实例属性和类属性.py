

'''
类属性的定义
'''
class Student(object):
      name = 'Student'   # 定义Student class的属性
a=Student()   # 创建Student class的instance:a, 那么a就有name为“Student"的属性
print(a.name)

'''
练习题:为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
'''