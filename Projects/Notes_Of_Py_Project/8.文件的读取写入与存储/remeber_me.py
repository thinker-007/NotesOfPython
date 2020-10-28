import json
user_name = input("请输入姓名：")

file = open("username.json", 'w')
json.dump(user_name, file)