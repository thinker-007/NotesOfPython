'''
上下文管理协议：context management protocol
      #  包含方法__enter__()和__exit__()，支持该协议的对象要实现这两个方法

上下文管理器：context manager
      #  支持上下文管理协议的对象，
      #  作用：用于规定某个对象的执行范围.可以在不需要文件的时候，自动关闭文件。
      #  语法形式：
            #  with...as...：执行with语句块context的进入和退出
            #  直接调用
'''
with open('text123.txt','w') as t123:  
      print(t123.closed)  #  查看文件是否关闭，file.closed是Boolean表达式
      t123.write('hello，一之')
print(t123.closed)  #  确实关闭了文件

#  自定义context manager
class Cm():   #  是一个类
      def __init__(self, filename, mode):
            self.fp = open(filename, mode)

      def __enter__(self):
            return self.fp

      def __exit__(self,exc_type, exc_val, exc_tb):
            self.fp.close()

cm = Cm('text123.txt','w')  #  定义实例
with cm as file:
      print(file.closed)
      file.write('hi,nihao')
print(file.closed)

###############################################
'''
contextlib模块：
      #  提供了更加易用的context manager
      #  通过生成器实现，不需要创建类以及__enter__和__exit__方法
'''
#  @contextmanager
from contextlib import contextmanager

@contextmanager
def make_open_context(filename, mode):
      fp = open(filename, mode)
      try:
            yield fp
      finally:
            fp.close()

with make_open_context('text123.txt', "w") as mytext:
      mytext.write('Good morning')
print(mytext.closed)

#  @closing: closing将任意对象变为context manager对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://math0.bnu.edu.cn/~ccxi/')) as page:
    for line in page:
        print(line)
