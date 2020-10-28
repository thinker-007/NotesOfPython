'''
带下划线的变量：
      #  前带_的变量:  标明是一个私有变量, 只用于标明, 外部类还是可以访问到这个变量
      #  前带两个_ ,后带两个_ 的变量:  标明是内置变量
      #  大写加下划线的变量:  标明是 不会发生改变的全局变量
      #  更详细的介绍见网页https://blog.csdn.net/qq_35290785/article/details/93476722
'''

'''
定制类：使用魔法方法(magical method)或者特殊方法(special method)增加class的方法如切片，选取对象,让class更接近list,tuple,set等class.
      #  使用一些带下划线的函数,即魔法方法或特殊方法：
            ##  __slots__：限制class的实例属性
            ##  __init__： 初始化实例
            ##  __str__：
            ##  __iter__ :使定义的类称为一个可迭代对象，即可使用for-in循环
            ##  __getitem__：可以象list一种取出其中的项
            ##  __getattr__
            ##  __call__
      #   参考网页https://wiki.jikexueyuan.com/project/explore-python/Class/magic_method.html
'''