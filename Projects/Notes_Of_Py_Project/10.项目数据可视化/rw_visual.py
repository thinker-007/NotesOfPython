#  绘制随机漫步的所有点（离散图）
'''
import matplotlib.pyplot as plt

from random_walk import Randomwalk 
gauss =  Randomwalk()
gauss.fill_walk()
plt.scatter(gauss.x_value, gauss.y_value)
plt.show()
'''

#  我们将上述稍微改一下（使用while循环），使得可以模拟多次（我们想要的次数）的随机漫步
'''
import matplotlib.pyplot as plt

from random_walk import Randomwalk 

while True:
      gauss =  Randomwalk()
      gauss.fill_walk()
      plt.scatter(gauss.x_value, gauss.y_value)
      plt.show()

      keep_running = input("继续随机漫步？(Y/N)：")
      if keep_running == "N":
            break
'''

#  设置漫步图的样式：
'''
给点着色:
'''
import matplotlib.pyplot as plt

from random_walk import Randomwalk 

while True:
      gauss =  Randomwalk()
      gauss.fill_walk()

      # 设置绘图的名称以及输出的尺寸
      plt.figure("随机漫步", figsize=(10, 6))
       
      #  点的标记
      point_numbers = list(range(gauss.num_points))
      plt.scatter(gauss.x_value, gauss.y_value, c=point_numbers, cmap=plt.cm.Blues,edgecolors=None)

      #  突出起点和终点
      plt.scatter(0,0, c="green", edgecolors=None)
      plt.scatter(gauss.x_value[-1], gauss.y_value[-1], c="red", edgecolors=None)

      #  隐藏坐标轴
      plt.axes().get_xaxis().set_visible(False)   # 隐藏x-轴
      plt.axes().get_yaxis().set_visible(False)   # 隐藏y-轴

      plt.show()

      keep_running = input("继续随机漫步？(Y/N)：")
      if keep_running == "N":
            break

'''
重新绘制起点和终点：见上面添加的代码
'''
'''
隐藏坐标轴：见上面添加的代码
'''
'''
增加点数：将5000改成50000或其它任意大的数字
'''
'''
调整尺寸以适合屏幕：见上面添加的代码
'''
