#  测试三阶最大公因子矩阵的行列式的值
import numpy as np

def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)

def my_code(x,y,z):
      for i in range(1,x):
            for  j in range(1,y):
                  for k in range(1,z):
                        if i<j and j<k:
                              M=np.array([[gcd(i,i),gcd(i,j),gcd(i,k)], [gcd(j,i),gcd(j,j),gcd(j,k)],[gcd(k,i),gcd(k,j),gcd(k,k)]])
                              det_M=np.linalg.det(M)

                              if det_M<0:
                                    print('there is a counter  example!')
                
      print('程序执行完毕！')

my_code(180,190,200)

#  上面使用nested loops解决多变量的循环
'''
多变量的循环的简单写法：
      #  使用zip()函数
      #  zip函数的原型为：zip([iterable, …])
      #  zip()的作用：参数iterable为可迭代的对象，并且可以有多个参数。该函数返回一个以元组为元素的列表，其中第 i 个元组包含每个参数序列的第 i 个元素。返回的列表长度被截断为最短的参数序列的长度。只有一个序列参数时，它返回一个1元组的列表。没有参数时，它返回一个空的列表。
'''
def my_codes(x):
      R=range(1,x)
      for i,j,k in zip(R,R,R):
            if i<j and j<k:
                  M=np.array([[gcd(i,i),gcd(i,j),gcd(i,k)], [gcd(j,i),gcd(j,j),gcd(j,k)],[gcd(k,i),gcd(k,j),gcd(k,k)]])
                  
                  det_M=np.linalg.det(M)

                  if det_M<0:
                        print('there is a counter  example!')
                        break
      print('程序执行完毕！')
my_codes(180)