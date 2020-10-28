# import numpy as np
# from numpy import random
# import matplotlib.pyplot as plt
# from scipy import stats
# from mpl_toolkits import mplot3d
# sum_two = lambda x,y: x+y
# print(sum_two(2,7))


# plt.figure('my_figure')

# arr_x = np.array([1, 2, 3, 4, 5, 4, 4])
# arr_y = np.array([8, 7, 6, 5, 7, 10, 32])

# p1 = plt.plot(arr_x, arr_y, marker = '*')
# plt.title('my son', fontweight='bold')
# plt.xlabel('your son')
# plt.legend(p1, 'cos')

# plt.show()


# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#   return slope * x + intercept

# mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

# plt.show()


# ax = plt.axes(projection='3d')

# #三维线的数据
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')
# plt.show()
# 导入turtle包的所有内容:
from turtle import *

screensize(400, 500, 'yellow')
# 默认起始点是屏幕中心，笔刷 pencolor('black'), width()
# 设置笔刷宽度与颜色
pensize(4)
pencolor('red')

pendown()
circle(-20, 180)
fillcolor("red")
begin_fill()
setheading(-12)
setheading(-145)
forward(30)
setheading(180)
circle(-20, 20)
setheading(143)
forward(30)
end_fill()
# 前进:
# forward(100)
# 右转90度:
goto(50, 30)
forward(100)
right(90)
circle(30, steps = 5)
# 笔刷颜色:
width(8)
pencolor('red')
forward(100)
right(90)

width(16)
pencolor('green')
forward(200)
right(90)

width(32)
pencolor('blue')
forward(100)
right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()


