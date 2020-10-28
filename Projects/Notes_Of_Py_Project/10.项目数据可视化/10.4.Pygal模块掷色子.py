'''
Pygal模块： gal是gallery(画廊)的简写
      #  使用python可视化包pygal可生成可缩放的矢量图形文件
      #  官方文档http://www.pygal.org/en/stable/,，单击Documentation,再单击Chartypes,就可以查看源代码了
      #  另外参考网站https://www.jianshu.com/p/08bf0efc3232
'''
'''
在文件die.py中创建Die class: 见文件
'''
#  建立Die的实例，即掷色子
from die import Die  # 导入Die class

die = Die()     #  定义Die的实例
results = []    #  定义掷色子结果的变量，初始值为空
for x in range(100):  #  掷100次色子
      result = die.roll()
      results.append(result)

print(results)

#  分析结果，如统计掷出n的次数
def num_count(value):
      num_counts = 0
      for y in results:
            if y == value:
                  num_counts = num_counts +1
            else:
                  continue
      return num_counts

print(num_count(6))

#  也可以调用count()函数
print(results.count(6))

results_seq = []
for x in range(1,7):
      results_seq.append(results.count(x))

print(results_seq)
#  利用pygal包将上述数据可视化
import pygal

hist = pygal.Bar()  #  条形图的实例
hist.title = "掷色子的结果的条形图"
hist.x_title = "掷色子的结果"
hist.x_lables = ['1', '2', '3', '4', '5', '6']
hist.y_lables = results_seq

hist.add('D6', results_seq)  #  将一系列值添加到图表中
hist.render_to_file('die_visual.svg')  #  复制文件路径用web打开