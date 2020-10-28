a=1
b=set(range(10))
for i in b: #for后面是表达式，与python的差异
    a=a+i
print(a)

def f(x):  #定义函数与matlab 的差异
    if x==1:
        return  1   #函数返回值与matlab的差异
    elif 0<x and x<1: #与matlab差异，elseif v.s. elif
        return 0
    else:
        return -1

print(f(1))

#计算前n项和, for-in循环
def sum_fun(n):

    a=0   #局部变量
    for i in range(n+1):
        a=a+i

    return a

print(sum_fun(100))

#判断n是素数的函数，for-else循环
def isprimer(n):
    for i in range(2,n):
        if n%i==0:
            return 'No' # 此处若不想出现No 可以用break语句替代
    else:
        return 'Yes'

print(isprimer(4))

#寻找n后面的第一个素数
def max_primer(n):
    for i in range(n):
        if isprimer(n+i)=='Yes':
            break

    return n+i



