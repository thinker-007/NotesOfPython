import json

with open('D:/zpython/tex.json') as f:
      new_file = json.load(f)   # 读取的数据存储到变量new_file中
print("读取到内存的数据：",new_file)