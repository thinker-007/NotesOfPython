'''
限制instance能添加的attribute(属性)：
      #  __slots__，即插槽。
'''
class Student(object):
      __slots__=("name","age")     # 用tuple定义允许绑定的attribute的名称
a=Student()
a.name="Gauss"
'''a.score=87  输出错误Student class没有相关属性'''
print("姓名是",a.name)

'''
__slots__的attribute限制只对当前class有用，对subclass不起作用
'''
class ChineseStudent(Student):
      pass
b=ChineseStudent()
b.name="张一之"
b.score=98
print("%s的得分为%s"%(b.name,b.score))   # 可以看到subclass 的属性并不受base class的限制

