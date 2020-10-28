'''''''''
模块:
      #  英文名：module
      #  一个模块就是一个.py文件，包含了python对象定义和python语句（definitions and statements）,如一个abc.py文件就是一个名字为abc的模块
      #  模块名存储在全局变量_name_中，是一个字符串（str）

模块的作用:
      #  模块封装一些相关的classes（class封装了一些方法(函数)），方便进行一些重复性的操作

模块的分类：标准的模块(python内置模块，英文为built-in module)，第三方模块以及自定义模块

'''''''''''''''''''''


'''''''''''''''''''''
包与其它的联系：
      包(package) > 子包(subpackage) > 模块(module) > 类(class) > 子类(subclass) > 实例(instance)
            #  类中可以封装一些方法，使得类中的实例可以调用这些方法

包（package）:
      #  封装模块的文件夹, 其中有一个文件__init__.py文件，这是和普通的模块包的差异
      mycompany  #  package_name
      ├─ web    #  subpackage_name
      │  ├─ __init__.py  #module_name
      │  ├─ utils.py
      │  └─ www.py
      ├─ __init__.py
      ├─ abc.py
      └─ utils.py

      #  www.py的模块名为Mycompany.web.www

      #  如左边map与educe.py的模块名为函数编程.高阶函数.map与reduce

      #  mycompany.web也是一个模块，对应web文件夹的第一个.py文件的模块

包的分类：标准包(python内置)，第三方包，自定义包

'''