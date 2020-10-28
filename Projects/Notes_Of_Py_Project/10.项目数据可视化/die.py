from random import randint  # 导入随机函数

class Die:
      def __init__(self, num_sides=6):  #  默认六面的色子
            self.num_sides = num_sides

      def roll(self):  #  定义方法：roll(转动)
            return randint(1, self.num_sides)  #randint(a,b)函数输出a-b之间的一个随机数
