'''
多重继承：一个subclass有多个base classes,那么这个subclass就继承多个base classes的方法
'''
class Animal(object):
      def move(self):    #  定义Animal class的一个方法（”技能“）
            print("我能动")
class  Drink(object):
      def drink(self):
            print("我能喝")
class Human(Animal, Drink):
      def human(self):
            print("我能吃")
Gauss = Human()
Gauss.move()   #  instance Gauss继承Animal class的方法move()
Gauss.drink()  #  instance Gauss继承Drink class的方法drink()
