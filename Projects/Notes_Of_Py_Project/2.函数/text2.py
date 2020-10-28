import datetime

starttime = datetime.datetime.now()
# def fib(x):
#       if x <= 2:
#             return 1
#       else:
#             return fib(x - 1) + fib(x - 2)

# ������ѭ���ķ����Ż���������

def fibo(n):
      a = 0
      b = 1
      s = 0
      x = 1
      while x <= n:
            s = a + b
            a=b
            b=s
            x = x + 1
      return s

n = input("您想知道第多少个的fibonacci数,请输入：")
n = int(n)       
answer = fibo(n)
print(answer)
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)   