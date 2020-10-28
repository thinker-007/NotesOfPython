names=['zhang', 'zhao', 'Li']

names.reverse()
print(names)

names.reverse()
print(names)

print('m\n''k')

a='H'
b=2
print('%s is not %s' %(a,b))
print('%s+%d' %(a,b))
print('还有%s天就放假了'% a)

print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
 
print("{0} {1}".format("hello", "world"))  # 设置指定位置
 
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置

string='my love is zhao'
print(string[3])
print(string[2:6])
print(string[1:9:2]) # 步长为2 注意与matlab切片的用法差异

t=(1,2,3)
print(t[2])

d={1:'ta',(1,2,3):'wo'}
print(d[1])

print(str(d))

d2={'father':'hua','mather':'nan'}
d.update(d2)
d.clear()
print(d)

s={1,2,3}
s.add(4)
print(s)

s.remove(1)
print(s)

s.discard(5)
print(s)

strings='my is is'
print(strings.replace('is', 'was', 1))