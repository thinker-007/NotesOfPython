#位置参数、默认参数、可变参数、关键字参数

#位置参数
def power(x):    #此处的x就是位置参数
      return x**2   #函数的返回值用return语句
def powers(x,n):  #此处x与n是位置参数
      s=1
      while n>0:
            n=n-1
            s=s*x
      return s      
print(power(2))   
print(powers(2,3))    

#默认参数:不在默认参数处输入时，采用默认值，必须放在位置参数后
def power_ss(x,n=2):  #此处n是默认参数，即不再n处输入默认为2
      s=1
      while n>0:
            n=n-1
            s=s*x
      return s
print(power_ss(5))    #计算5^2
print(power_ss(2,3))
def add_list(L):
      L.append('张耀华')    #list L最后加上张耀华 
      return L
print(add_list(['赵胜男']))
def add__list(L=[]):    #设置L的默认参数为空list'[]'
      L.append('张耀华')    #list L最后加上张耀华 
      return L
print(add__list())  #不输入参数按默认参数计算，输出["张耀华"]
print(add__list(["赵胜男"]))  #此时L默认值["张耀华"]，输出["张耀华","张耀华"]，
def add___list(L=None):   #设置L的默认参数为空list'[]'，None没有任何类型
      if L is None:
            L = []
      L.append('张耀华')    #list L最后加上张耀华 
      return L
print(add___list())  #不输入参数按默认参数计算，输出["张耀华"]
print(add___list())

#可变参数，即传入的参数的个数是可变的
def variable(var):    #var取list类型（如[1,3,2]）或tuple型（如(4,5,6)）或set（如{9,8,7}）
      s=0    
      for a in var:
            s=s+a
      return s    #对var(list or tuple or set)中的数求和
print(variable({1,2,3}))   #输出结果6
def variables(*var):    #通过*var变成可变参数,它是一个tuple
      s=0    
      for a in var:
            s=s+a
      return s   
print(variables(1,2,3))  #输入一组数字，不必是某个类型
# print(variables({1,2,3}))   #显示错误
print(variables(*{1,2,3}))    #要将set变成可变参数，左上角上加*，函数调用时转换成tuple

#关键词参数，即传入任意含参数名的参数，必须有参数名并赋值
def person(name,age,**kw):   #**表示关键字参数,可以任意添加，它是一个dict(输出)
      print('name:',name,"age:",age,"others:",kw)
person("一之",1,出生地='湖北',关系='赵胜男的儿子')   #后两项是可选项

#命名关键字参数，限制关键字参数的参数名，它和位置参数的差异是输入时不能省略参数名
def persons(姓名,age,*,出生地,关系):  #*后面称为命名关键字参数，须输入参数名
      print(姓名,age,出生地,关系)
persons("一之",1,出生地='湖北',关系='赵胜男的儿子')   #不能省略出生地，关系参数名
def person_s(姓名,age,*,出生地="北京",关系):  #出生地设置成默认值
      print(姓名,age,出生地,关系)
person_s("一之",1,关系='赵胜男的儿子')

#参数组合
    ##函数可以使用组合参数，顺序是必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def person_ss(name, age,*,city,**kw):
    if 'city' not in kw:
        pass   # 有city参数
    print('name:', name, 'age:', age, "city:",city,'other:', kw)
person_ss('Jack', 24, city='Chaoyang', zipcode=123456)

#计算多个数的乘积
def  products(*var):    #参数仍是var,*标注类型
      s=1
      for a in var:    
            s=s*a
      return s
print(products(1,4,6,8))