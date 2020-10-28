'''
subclass与baseclass
      #  被继承的称为base class, 继承的称为subclass

class Animal(object):   #蓝绿色为类,表示Animal class继承object class
      pass
class Dog(Animal):   #Dog class继承Animal class
      pass

'''

'''
继承的用处：subclass继承base class的全部功能。
'''
class  Animal(object):
      def name(self):   #定义class中方法name(),变量必须是self,即instance
            print("我是动物")
class Dog(Animal):  #Oog subclass继承Animal class的name()函数
      pass         
dog=Dog()       #定义Dog class中的instance
dog.name()      #输出“我是动物”
'''print("第二种=",name(dog))  这种调用方法是错的'''


'''
subclass 的方法覆盖base class的方法：
'''
class Cat(Animal):  #定义Animal的subclass Cat
      def name(self):
            print("我是猫")
cat=Cat()   #定义Cat class的一个instance:cat
cat.name()  #对象按name()的方法操作，输出“我是猫”，覆盖base class 的方法

'''
多态:
      #  subclass 的instance 也是base class的instance,所以subclass 的instance既可以使用subclass的方法，也可以使用base class中的方法。
      #  下面中的gary猎犬既是Dog class的instance,又是Animal class的instance
      #  定义一个class,我们就定义了一个数据类型，其与python自带的数据类型list,tuple，dict等没什么两样。
'''
a=list()  #可以理解为list class 中的instance
ant=Animal()  #ant蚂蚁是Animal class的instance
gary=Dog()    #gary猎犬是Dog class的instance

'''
检验数据类型：isinstance(), 是否是instance
'''
print(isinstance(a,list))    #a是否是list class中的instance,输出True
print(isinstance(gary,Animal))  #gary是否是Animal class的instance，输出True

'''
多态的好处
      # 我们在base class 数据类型上定义函数，后面定义的subclass可以调用而不必更函数
      # “开闭”原则：对扩展开放，允许增加subclass; 对修改封闭,不必修改base class 的函数
'''
def  names(x):   # 出入Animal 型数据,即Animal class的instance
      x.name()
      x.name()
frog=Animal()   # 定义Animal class的instance：frog 青蛙
names(frog)     # 注意names()是外部函数，不是class中的方法，不能调用为frog.names()
pug=Dog()       #  定义Dog class的instance:pug 哈巴狗
names(pug)      # 可以作为Animal类型数据，可以点用names()函数