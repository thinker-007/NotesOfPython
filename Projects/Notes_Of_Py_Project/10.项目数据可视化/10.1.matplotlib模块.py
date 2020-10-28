'''
模块pyplot:
      #  一般模块pyplot指定别名plt
            import matplotlib.pyplot as plt
      #  plt.figure(figure_name的str):  图的名称
      #  plt.subplot(subplot_name的str):  创建子图
            plt.subplot(numrows、numcols、fignum)
            numrows:图形的行数,即number of rows
            numcols:图形的列数，即number of columns
            fignum:当前子图的编号
      #  plt,plot()具有画折线图功能，基本格式
      plt.plot([x](option), [y], 线条颜色(option), 线条粗细(option))
      [x]具有默认值
      #  plt.scatter()具有画散点图的功能
      #  plt.hist()具有画直方图的功能
      #  plt.show()方法打开matplotlib查看器
      #  控制线的属性：线宽，线的形状，平滑等
      #  参考网站https://blog.csdn.net/qq_31192383/article/details/53977822或者https://blog.csdn.net/xHibiki/article/details/84866887
      
'''
#######################################################
'''
折线图: plt.plot()
'''
import matplotlib.pyplot as plt

plt.figure("text")
plt.subplot(221)
x = [2,3,4]
y =  [2*a for a in x] 
plt.plot(x, y)

plt.subplot(223)
y = [2.5,3,5]
plt.plot(y)  # 默认x的list[0,1,2]
plt.show()   #  关闭第一个figure后就会显示此折线图

################################################
'''
散点图: plt.scatter
'''
plt.figure("散点图的例子")
x = [2,3,4]
y = [10,17,19]
plt.scatter(x, y)
plt.show()
######################################################
'''
直方图：plt.hist()
水平直方图：plt.barh()
条形图：plt.bar()
饼图：
      #  可参考网页https://blog.csdn.net/yywan1314520/article/details/50818471
      #  直方图、条形图、饼图的绘制可参考https://blog.csdn.net/hohaizx/article/details/79101322
      #  关于中文的问题见网站https://www.jb51.net/article/136397.htm
'''
from pylab import *    #  加载中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.figure("条形图的例子")
plt.title("Bar graph")
plt.xlabel("姓名")
plt.ylabel('亲密度')
x = ["张耀华", "赵胜男", "张一之"]
y = [28, 34.5, 78.9]
plt.bar(x, y)
plt.show()
#####################################################
'''
多曲线与多图模式：
'''
plt.figure("多曲线的例子")
plt.title("多曲线的例子")  
x1 = [1,2,3]
y1 = [7,8,9]
x2 = [4,5,6,8]
y2 = [16, 23,78,100]
plt.plot(x1,y1, 'r-',x2,y2,'g--')
plt.show()
 
#  多图的例子见上面

#####################################################
'''
图形的修饰：控制线、坐标轴，表头字符串，坐标抽字符串，坐标抽标记等属性
      #  参考网页https://blog.csdn.net/qq_31192383/article/details/53977822
      #  参考网站https://blog.csdn.net/xHibiki/article/details/84866887
'''

'''控制线的属性：线宽，线的形状，平滑等'''
# 方法一：使用关键字参数
''' plt.plot(x, y, linewidth =2.0)'''

# 方法二：对线对象(Line2D)使用set_方法，

# 方法三： 使用setp()命令
'''
      lines = plt.plot(x1, y1, x2, y2)
      plt.setp(lines, color='r', linewidth=2.0)
参见上述Line2D属性及其取值
'''

#######################################################
''' 
添加文字:
      #  plt.title(): 修饰表头
         plt.title(表头字符串, 修饰参数)
      #  plt.xlable(x轴字符串, 修饰参数)
      #  plt.ylable(y的字符串, 修饰参数)
      #  text()命令可以在任何位置添加文字
'''
'''
控制坐标轴与轴上标记的属性：   
      #  参见网页https://blog.csdn.net/HHG20171226/article/details/101294381
      #  plt.axis(): 设置坐标轴参数
      #  plt.tick_params(): 设置坐标轴标记参数，如字体大小
            plt.tick_parama(axis = 'x'('both'), 其它修饰参数)
'''
#########################################################
'''
自动计算数据：
'''
plt.figure('平方函数')
plt.title("平方函数")
X = list(range(1,1001))
Y = [x**2 for x in X]   #  注意幂次的记号不是x^2，而是**
plt.plot(X, Y)
plt.show()

'''
删除数据点的轮廓：
      #  实参edgecolor = 'none'
'''
'''
使用颜色映射：
'''
############################################################
'''
自动保存图表：plt.savefig()
'''


