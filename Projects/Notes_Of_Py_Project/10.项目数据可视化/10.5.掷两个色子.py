from die import Die
die1 = Die()
die2 = Die()

results = []   #  100次的点数
for x in range(1,101): 
      result = die1.roll()+die2.roll()
      results.append(result)

frequencies = []
for n in [2,3,4,5,6,7,8,9,10,11,12]:
      frequencies.append(results.count(n))

print(frequencies)

import pygal

hist = pygal.Bar()  #  条形图的实例
hist.title = "掷两个色子的结果的条形图"
hist.x_title = "掷两个色子的结果"
hist.x_lables = [2,3,4,5,6,7,8,9,10,11,12]
hist.y_lables = frequencies

hist.add('D6+D6', frequencies)  #  将一系列值添加到图表中
hist.render_to_file('die12_visual.svg')  #  复制文件路径用web打开