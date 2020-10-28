import json

f = open("username.json",'r')
user_name = json.load(f)
print("welcome come back!"+user_name)