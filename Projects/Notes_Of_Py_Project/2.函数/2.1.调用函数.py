                        #调用函数

#求圆的面积的例子
r=[1,2,3]
n=2
while n>=0:   #while循环
      s=3.14*r[n]**2
      print('半径为%s时圆的面积为%s'%(r[n],s))
      n=n-1
for a in r:   #for-in循环
      squ=3.14*a*2
      print('半径为%s时圆的面积为%s'%(a,squ))

#获取函数信息,通过交互命令行获取信息help(abs)

#调用函数，如前面的数据类型函数set()、int()、float()，输出函数print(),输入函数input()
      ##进制转化函数hex()