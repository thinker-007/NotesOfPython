'''
requests包：
      #  python第三方库
      #  详情可见官网https://requests.readthedocs.io/zh_CN/latest/
'''
'''
url:
      #  统一资源定位符
      #  是一个给定的独特资源在Web上的地址。每个有效的URL都指向一个独特的资源。这个资源可以是一个HTML页面，一个CSS文档，一幅图像，等等
      #  url的实例：
            https://developer.mozilla.org
            https://developer.mozilla.org/en-US/docs/Learn/
            https://developer.mozilla.org/en-US/search?q=URL
      #  url的组成：

            http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument

            http:// 是协议。它通常都是HTTP协议或是HTTP协议的安全版，即HTTPS。Web需要它们二者之一，但浏览器也知道如何处理其他协议，比如mailto:（打开邮件客户端）或者 ftp:（处理文件传输），
            www.example.com 是域名。 它表明正在请求哪个Web服务器。
            :80 是端口。 它表示用于访问Web服务器上的资源的技术“门”。如果Web服务器使用HTTP协议的标准端口（HTTP为80，HTTPS为443）来授予其资源的访问权限，则通常会被忽略。否则是强制性的。
            /path/to/myfile.html 是网络服务器上资源的路径。
            ?key1=value1&key2=value2 是提供给网络服务器的额外参数。 这些参数是用 & 符号分隔的键/值对列表。
            #SomewhereInTheDocument 是资源本身的另一部分的锚点. 锚点表示资源中的一种“书签”，给浏览器显示位于该“加书签”位置的内容的方向。
      #  参见网站https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/What_is_a_URL
'''
import requests

#  添加请求头，原因参见https://blog.csdn.net/weixin_43902320/article/details/104342771和https://blog.csdn.net/SpringRolls/article/details/80554610
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url,headers=headers)
 
print("status code:", r.status_code)  # 状态码核实调用是否成功,显示200表示成功

#  存储响应的数据
response_dict = r.json()  #  使用json方法

#打印结果
print(response_dict.keys())  

#  处理数据response_dict
