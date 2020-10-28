                        #1.条件判断（if语句）

'''  if 语句语法：if ...else...:从上向下执行语句  '''
age=30
if age>=18:
      print('你的年龄是', age)
      print("adult")
if age<18:     #  也可将此句换成 else:
      print("你的年龄是", age)
      print('teenager')

'''   另外可用elif进行更细致的分类   '''
age1=7          #注意标点是英文输入
if age1>=18:
      print('adult')
elif age1>=6:
      print('teenager')
elif age1>=2:
      print('kid')
else:
      print('婴儿')

                        #再议input()

      #input返回str(字符串)，没法进行判断，需要转换数据类型(int()函数)
s=int(input("输入你的出生年份："))
if s>=2000:
      print('00后')
else:
      print('00前')
