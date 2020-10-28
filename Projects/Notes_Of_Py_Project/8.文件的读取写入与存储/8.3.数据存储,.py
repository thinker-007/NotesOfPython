'''
模块json:
      #  参见网站https://www.jianshu.com/p/e29611244810
      #  JSON是一种数据交换格式
      #  模块json是python 内置模块
      #  模块json可以将简单的python数据结构转存到文件中，并在程序再次运行时加载该文件中的数据
      #  模块json的两个方法：dump()与load()
'''
####################################
'''
json.dump()：存储
      #  使用json方法，首先要导入json模块
      #  此方法接受两个实参，其格式为json.dump(data_name, file_name), data_name是要存储数据的名称，file_name是用于存储数据的文件名称
'''
import json

L = [3, 5, 7, 9, 1]

file_name = open("tex.json", 'w+')   # 打开一个json文件，用于存储数据
json.dump(L, file_name)       #  创建tex.json文件

##########################################
'''
json.load(): 读取到内存
      #  接收一个参数：json.load(文件名)
      #  见文件number_reader.py
'''
###########################################
'''
保存和读取用户生成的数据：
'''

