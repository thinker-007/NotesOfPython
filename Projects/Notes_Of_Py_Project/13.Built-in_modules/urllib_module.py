'''
urllib模块：
      #  提供了用于操作URL的功能，基本上涵盖了基础的网络请求功能
      #  主要模块：
            #  request module:主要负责构造和发起网络请求
      #  详情参见网站https://blog.csdn.net/jiduochou963/article/details/87564467
'''
#############################################
'''
request module:
      #  实用模块中的urlopen()函数发起网络请求
'''
from urllib import request

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

douban_web = request.urlopen('https://www.douban.com')  #  存储网站返回的值  
tex = douban_web.read()   #  返回一个http.client.HTTPResponse对象,用此对象的read()打开
tex1 = tex.decode()  #  tex是二进制文件，需实用方法decode()转换成字符串格式
print(tex1)

###############################################
'''
response module:
'''
###############################################
'''
parse module:
'''
################################################
'''
error module:
'''
#################################################