'''
文件的打开：
      #  使用关键词with：读取的文件仅被with下面的代码块使用
            with open(文件名(无后缀)， 读写模式) as 别名:  #  注意冒号
      #  直接使用open()
'''
with open(r'D:\zpython\8.文件的读取写入与存储\x.txt') as file_bieming:
      pass
bieming = open(r'D:\zpython\8.文件的读取写入与存储\x.txt')

##############################################################
'''
文件的读取：
      #  read(), 
      #  readline(),
      #  readlines()
'''
#  read(): 一次性读全部的数据
with open(r'D:\zpython\8.文件的读取写入与存储\x.txt') as e:  #  后面有冒号
      a = e.read()
      print("第一次读的文件：", a)
h = open('D:/zpython/8.文件的读取写入与存储/x.txt')  #  后面没有冒号
d = h.read()
print("第一次读的文件：",d)

#  readline(): 读取第一行
f = open(r'D:\zpython\8.文件的读取写入与存储\x.txt')
b = f.readline()
print("第二次读的文件：",b)

#  readlines(): 读取所有行，并输出list类型数据
g = open(r'D:\zpython\8.文件的读取写入与存储\x.txt')
c = g.readlines()
print("第三次次读的文件：",c)

#  使用for-in循环读取多行；
j = open(r'D:\zpython\8.文件的读取写入与存储\x.txt')
for line in j:
       print(line.rstrip())
''' print(line)   #  这样输出的行与行之间会空一行'''

#########################################     
'''
注意事项：
      #  写出文件的绝对路径
      #  文件名中有转义符‘\’,需要用去转义符r' ',或者用’/‘去替代’\‘.
      #  调用文件行时有点象generator, 即每次调用从上次结束的地方开始
'''
################################################
'''
创建一个包含文件各行内容的列表
      #  使用关键词with时，open()打开的文件对象只在with代码块里可用。若要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表。见readlines().
'''