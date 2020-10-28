'''
迭代：
    ## 迭代：通过for-in循环来遍历list或tuple或其它可迭代数据(dict或字符串)的运算
'''
    ##dict的迭代,dict有key与value两部分
d={"张耀华":"爸爸","赵胜男":"mama","一之":"儿子"}
for a in d:
      print(a)  #dict中迭代的是key,输出key
print(d.values())
for v in d.values(): #使用dict的取values操作
      print(v)       #迭代values

'''
可迭代对象的判断
'''
from collections.abc import Iterable   # 注意class的名字是大写，小写会报错
print("\'abc\'是否是可迭代的", isinstance('abc', Iterable))  # 可迭代

'''
双变量循环
'''
for i, value in enumerate(['A', 'B', 'C']): #内置的enumerate函数把一个list变成索引-元素对
      print(i, value)
for X,Y in {(1,2),(3,4)}:
      print(X,Y)  #不带括号
      print((X,Y))  #带括号

'''
例子：寻找list中最大与最小值，输出tuple
'''
def find_minmax(L):
      s=L[0]
      t=L[0]
      for a in L:
            if a<=s:
                  s=a
            if a>t:
                  t=a
      return (s,t)
print(find_minmax([4,2,1,3]))    

