'''
python中与处理时间相关的模块
      #  time
      #  datetime
      #  calendar
      #  关于time模块参见网站https://blog.csdn.net/you_are_my_dream/article/details/61616465
'''
############################################################
'''
datetime模块：
      #  Built-in module. 提供了操作日期和时间功能。
      #  较详细的介绍参见网站https://www.jb51.net/article/147429.htm
      #  主要有如下的类：date, time, datetime, datetime_CAPI, timedelta, timezero
      #  使用场景：
'''
'''
date类:由year年份、month月份及day日期三部分构成
'''
from datetime import date

a = date.today()  # 调用date类中的today()方法
print(a)
''' 
datetime类
'''
from datetime import datetime

#  获取当前日期和时间
today1 = datetime.today()
print(today1)
now = datetime.now()  #  怎么从class, instance这一角度理解
print(now)

#  获取指定时间和日期
dt = datetime(2005, 4, 11, 7, 23, 56)  # dt是datetime实例
print(dt)

#  datetime与timestamp(时间戳)间的转化
      # timestamp(时间戳)是指格林威治时间自1970年1月1日（00:00:00 GMT）至当前时间的总秒数可参考网站https://blog.csdn.net/qq_41651465/article/details/80005362
dt_stp = dt.timestamp()   #  使用类中方法timestamp()
print(dt_stp)
now_stp = now.timestamp()
print(now_stp)
t = 1429417200.0 
stp_t = datetime.fromtimestamp(t) #使用fromtimestamp()方法,注意t不是实例，调用方法格式注意
print(stp_t)

#  str与datetime的转化： 格式化转化
str1 = '2020-12-31 12:12:12'
str1_translate_datetime = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S')  # 使用strptime方法,格式要一致
print(str1_translate_datetime)

now_trans_str = now.strftime('%a, %b %d %H:%M')
print(now_trans_str)

'''
timedelta类： 时间的加减
'''
from datetime import timedelta

now_plus = now + timedelta(days=2, hours=14)
print(now_plus)

'''
timezero类：
'''