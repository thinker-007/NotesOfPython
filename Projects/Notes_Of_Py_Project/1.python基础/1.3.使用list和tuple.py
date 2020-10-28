'''''''''
1.list
    list:一种有序的集合，其中元素可以是不同类型，可以随时添加或删除其中的元素，用[]表示。用len()函数可以计算list中元素的个数。
'''
''' 1.1.定义班级人数的list:classmates'''
classmates=["张耀华","赵胜男","一之"]
  
''' 1.2.计算list元素个数'''
len(classmates)   #输出3
  
''' 1.3.提取list中元素,从0开始'''
classmates[1]   #输出赵胜男

''' 1.4.从倒数获取元素'''
classmates[-1]  #输出倒数第一个一之
classmates[-2]  #输出倒数第二个

''' 1.5.在list中插入元素（使用insert和append）'''
classmates.insert(1,'九之')   #在1号位插入“九之”
classmates.append(2)   #在list最后位置添加2

'''1.6.删除指定元素（使用pop）'''
classmates.pop(1)   #删除第一号位‘九之’，pop有出的意思
classmates.pop()    #删除最后一个“一之”

''' 1.7.替换元素（直接重新定义）'''
classmates[1]="刘想枝"   #第一号位换成刘想枝

'''  1.8.list的嵌套'''
p=[1,2,3]  #定义一个新list
classmates[1]=p    #插入一个list
classmates[1][0]   #输出数字1

'''''''''
2.tuple
      tuple:有序列表，称为元组，它与list很相似，但初始化后，不可对元素进行操作。
'''
''' 2.1.定义tuple'''
t1=('张耀华','赵胜男')
t2=(1,2)
t3=('一之',)   #定义一个元素的tuple必须加逗号

'''2.2.空tuple'''
T=()
  
'''2.3.tuple中嵌套list'''
k=[9,8,7]
t4=(k,4,5)
#  我们可对tuple中的list 操作
'''t4(1)[1]=10  #不能操作'''
k[1]=10      #可以修改t4