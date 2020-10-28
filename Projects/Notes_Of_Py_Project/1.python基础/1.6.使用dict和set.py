                        #使用dict和set
'''
Dict
   ##  dict:是dictionary(字典)的缩写，类似于其它语言的map,key-value
   ##  格式：dict_name={key1:value1, key2:value2,...}
   ##  相关操作：更新、查找、判断、排序
'''      

'''    
建立dict,如下面的成绩表，注意dict中的key是不变的，因此不能是list,set,dict
'''
D={"张耀华":'father','赵胜男':'mather','一之':'son'}  
print("D=",D)    #print()中取名要用逗号隔开
print(D)
d={'张耀华':78,"赵胜男":93,"一之":100} 
print(d["一之"])   #查找一之的成绩，用中括号
      ##更新与添加元素
d["一之"]=150     #更新一之的成绩为150
print(d)
d['九之']=200     #若dict中没有元素则添加
print(d)
# d.insert("二之":300)    #使用insert()函数添加错误
# print(d)

'''
判断元素：使用in或者get()函数
      本质上get()是最大的类object的方法，Dict是object的subclass,那么Dict class 继承object的方法，也就是有get()的方法
'''
print('刘想枝' in d)    #要输出结果必须使用print()函数，结果为false
print(d.get('刘想枝'))     #对数据的操作格式，前面也见过,返回None表示没有
print(d.get('一之'))      #返回100，即有一之的成绩并输出

'''
删除元素：用pop(),与对list的操作同
      道理与get()类似
'''
d.pop("一之")      #删除key,其对应value也删除
print(d)

'''''''''
set,即集合
    ##基本操作列表转集合set()、添加元素add()、删除元素remove()、集合运算
'''
L=[1,2,3]
S=set(L)
print(S)
S.add("一之")
print(S)
S.remove(1)
print(S)

'''集合的并“|”“union”，交“&”“intersection”，差“-”“difference”'''
s1={1,2,3,5,4}
s2={2,4,6,8}
print(s1.union(s2))    #注意Python中对数据的操作格式：“数据.操作命令”
print(s1 | s2)
print(s1.intersection(s2))
print(s1 & s2)
print(s1.difference(s2))
print(s1-s2)
      ##逻辑判断