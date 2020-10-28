#sort()
      ##即排序算法

#默认排序,从小到大
L=sorted([-2,-4,7,4,-5])
print("L=",L)

#反向排序
L1=sorted([-2,-4,7,4,-5],reverse=True)
print("L1=",L1)

#在key函数要求下排序
L2=sorted([-2,-4,7,4,-5],key=abs)  #绝对值排序
print("L2=",L2)
L3=sorted(["张耀华","老婆赵胜男","儿子一之"],key=len,reverse=True)
print("L3=",L3)

#例子：对成绩排序
  ##按成绩排名
L4=[("二张耀华",75),("一赵胜男",50),("张一之",60)]
def  score(t):   #定义排序的key函数
      return t[1]
L5=sorted(L4,key=score)
print("L5=",L5)
  ##按姓名排名（字符串是按ASCI大小排序）
def name(t):
      return str.lower(t[0])
L6=sorted(L4,key=name)
print("L6=",L6)