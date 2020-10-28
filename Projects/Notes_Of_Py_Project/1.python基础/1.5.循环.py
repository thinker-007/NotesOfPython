                    #循环

'''
  for-in循环，把list或tuple中的每个元素迭代出来  
'''
names=['张耀华','赵胜男','一之']
for a in names:
      print(a)   #输出三个名字

     #计算多项和
names=[1,2,3,4]
sum=0
for a in names:    #循环执行下面两行代码
      sum=sum+a 
      print(sum)    #输出每一步的sum:1 3 6 10
print(sum)         #输出最后的sun

      #生成整数序列函数range()
L=list(range(101))      #list(),int(),float()数据类型转化函数
print(L)
R=range(4)
print(R)  
sum=0
for a in L:
      sum=sum+a
print(sum)        #输出1+2+3+...+100的结果

''' 
  while循环，只要条件满足就执行代码块，否则退出执行下一步  
'''
sum=0
n=100
while n>0:
      sum=sum+n
      n=n-1    #n自减进行循环
print(sum)     #输出1+2+3.。。+100的结果

L=['张耀华','赵胜男','一之']
for a in L:
      print("hello,", a,"!")

''' 
 break语句，提前退出循环  
'''
n=1
while n<=100:
      if n>10:   #执行下面缩进的代码块
            break
      print(n)
      n=n+1
print('END')     #结束记号

'''
continue语句，结束此轮循环进行下一步循环，不执行continue下面的语句（如下面的print()）
'''
n=100
while n>10:
      n=n-1       #循环语句
      if n%2==0:   #n%2表示除以2的余数
            continue  #  continue指的是继续循环
      print(n)    #输出100以内大于10的奇数

'''
for-in死循环的例子
L=[1,2]
for a in L:     #在list L最后一项加上3
      L.append(3)  
      print(L)
'''

'''
while的死循环的例子
sum=0
n=int(1)
while n>0: 
      n=n+1
      sum=sum+1
      print(sum)    #输出所有的sum
'''

