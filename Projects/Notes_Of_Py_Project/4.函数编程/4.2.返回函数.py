'''
内嵌函数（nested function）
      #  指在另一个函数里定义的函数，如下面sum()是lazy_sum的内嵌函数
      #  内嵌函数可以访问外部函数(outer enclosing function)的范围内的变量，这些变量称为非本地变量（nonlocal variable）
'''
def print_msg(msg):    #outer enclosing function，外部闭包函数
      def printer():   #nested function 无本地变量
            print(msg) #访问outer enclosing function 的变量
      return printer   #返回函数
another=print_msg("Hello")  #传入"Hello"调用print_msg函数,返回的函数被命名为another
print(another())            #调用another 函数，可以看到  


#函数作为返回值
def lazy_sum(*args):   #对可变参数求和
      def sum():       #内部函数无本地变量
            ax=0
            for x in args:  #内部函数sum()引用了外部函数lazy_sum的变量args
                  ax=ax+x
            return ax
      return sum      #返回内部函数sum()的名称,参数和变量都保存在返回的函数中
f=lazy_sum(1,2,3)
print("f=",f)        #输出求和函数
print(f())           #输出和6
######################################
'''
闭包（closure）
      ##  一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包（Closure）。
'''
'''
怎样得到一个闭包函数
      ##内嵌函数使用非本地变量
      ##闭包函数满足三个标准：(1) 必须有一个nested function；(2) nested function必须引用一个定义在闭合函数范围内的非本地变量；(3) 外部函数必须返回nested function.
'''
'''
什么时候用closure
      #  可以减少使用全局变量和提供一定程度的数据隐藏
      #  当一个类只有很少的办法（通常只一个），closure可以提供更优雅的替代方案。但如果内的属性或者方法开始增多，最好还是实现一个类。
'''
def make_multiplier_of(n):    #定义闭包函数
      def multiplier(x):       #本地变量
            return x*n
      return multiplier      
times3=make_multiplier_of(3)   #定义乘3的函数名为times3
a=times3(5)                    #输入5调用times3函数
print("a=",a)

#例子：利用闭包函数返回一个计数器函数，每次调用它返回递增整数