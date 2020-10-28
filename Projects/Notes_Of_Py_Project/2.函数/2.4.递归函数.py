'''
递归函数，即函数在自身内部调用自身
   #  计算n的阶乘
'''
def fact(n):   #递归算法
      if n==1:     #注意python语言中“=”表示赋值，“==”表示逻辑判断
            return 1
      return n*fact(n-1)
print(fact(4))   #计算4！
def facts(n):      #也可采用循环语句
      s=1
      while n>=1:
            s=s*n
            n=n-1
      return s
print(facts(4))

'''''''''
栈（stack）:数据结构
    #  函数调用是通过栈这种数据结构实现的，调用一次函数增加一个栈帧
    #  栈溢出：栈的大小有限，递归次数太多会出现栈溢出
'''
print(facts(1000))  #循环算法正确输出结果
#print(fact(1000))   #递归算法显示溢出
'''
尾递归优化: 解决递归算法的栈溢出
     #  尾递归是指在函数返回的时候，调用函数自身且return语句不能包含表达式
'''
def facts_s(n):
      return fact_iter(n,1)

def fact_iter(num,product):   #实际上是循环
      if num==1:
            return product
      return fact_iter(num-1,num*product)
print(facts_s(4))

'''
例子：汉诺塔的移动
'''
def move(n,a,b,c):   #注意变量
      if n==1:
            print(a,'-->',c)
      elif n>=2:
            move(n-1,a,c,b)
            print(a,'-->',c)
            move(n-1,b,a,c)
print(move(3,"A","B","C"))
      
