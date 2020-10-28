# 建立狗类

class Dog():
    #初始化属性：名称，年龄，产地（默认中国）
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.region='china' #默认属性的写法

    #定义相关功能
    #叫汪汪
    def cry(self):
            print('wangwang') 
    
# 实例化
# my_dog=Dog('xiao',2)
# print(my_dog.cry())  #调用cry方法
# print(my_dog.region)

# my_dog.region='USA' #通过直接赋值更改属性
# print(my_dog.region)

#子类
class Male_dog(Dog):
    #继承,必须继承父类所有属性,可以添加新属性
    def __init__(self,name,age,temper):
        super().__init__(name,age)
        self.temper=temper 
    #子类重新定义cry方法
    def cry(self):
        return 'heihei'

your_dog=Male_dog('zhang',23,'crazy')
print(your_dog.region) #调用属性，父类属性
print(your_dog.cry())  #调用方法，比较与调用属性的差异

'''将实例用作属性'''
#定义一个独立类：腿类
class Leg(): 
    def __init__(self,type_leg, number_leg):
        self.type_leg=type_leg
        self.number_leg=number_leg

class Female_dog(Dog):
    # self.type_leg='long'
    # self.number_leg=4
    #上两行属性定义可由下面的实例化实现
    def __init__(self,name,age,type_leg, number_leg):
        super().__init__(name,age)
        self.leg=Leg(type_leg, number_leg) #实例化定义，用圆点表示法访问leg属性

his_dog=Female_dog('Jack',13,'long',4)

print(his_dog.leg.type_leg)
print(his_dog.leg.number_leg)