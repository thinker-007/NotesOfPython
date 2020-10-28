'''
列表生成式--range()
      ##即list Comprehensions,可以创建list的生成式
''' 
print([x * x for x in range(1, 11)])  #for-in循环生成list
# print((x * x for x in range(1, 11)))  生成不了tuple
print({x * x for x in range(1, 11)})   #可以生成集合
print({m+n for m in "ABC" for n in "abc"})  

'''
items()函数,遍历输出dist中的（key,value）
      #  item()是class Dict中的方法
'''
d={"张耀华":'father','赵胜男':'mather','一之':'son'}
print(d.items())
for x,y in d.items():  
      print(x)        #输出key值 
      print(y)        #输出value值
for x in d.items():  #单变量输出（key,value）
      print(x)

'''
生成两个变量的列表
'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

'''
if...else生成列表
'''
print([x for x in range(1, 11) if x % 2 == 0])   #if是循环语句的筛选条件
print([x if x % 2 == 0 else -x for x in range(1, 11)])  #不能省掉else