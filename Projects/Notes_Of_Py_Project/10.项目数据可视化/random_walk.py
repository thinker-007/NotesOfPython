from random import choice   #  导入随机生成函数choice()

class Randomwalk():
      def __init__(self, num_points = 5000):
            self.num_points = num_points
            self.x_value = [0]
            self.y_value = [0]

      def fill_walk(self):  #  定义方法：存储漫步包含的点，并决定每次漫步的方向
            while len(self.x_value) < self.num_points:
                  x_dir = choice([1,-1])   # x轴方向，随机选择
                  x_dis = choice([0,1,2,3,4])  # x方向步数，随机选择
                  x_step = x_dir*x_dis     # 由上面决定的x方向随机步数

                  y_dir = choice([1,-1])   # x轴方向
                  y_dis = choice([0,1,2,3,4])  # x轴间距
                  y_step = y_dir*x_dis 

                  if x_step == 0 and y_step == 0:  # 拒绝原地踏步，跳过原点
                        continue

                  next_x = self.x_value[-1] + x_step  #  在前一步基础上前进
                  next_y = self.y_value[-1] + y_step

                  self.x_value.append(next_x)
                  self.y_value.append(next_y)