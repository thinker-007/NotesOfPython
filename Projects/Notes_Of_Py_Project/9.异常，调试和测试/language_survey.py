#########  使用AnonymousSurvey类#######################
'''
from survey import AnonymousSurvey
question = "你的母语是什么？"
my_survey = AnonymousSurvey(question)  #  定义调查实例，即调查什么

response = input("您的母语：")
my_survey.store_response(response)  #  存储答案
my_survey.show_results()     #输出答案

'''
'''
上述程序的问题是只有一次的调查便结束程序。
用循环语句进行多次调查。

from survey import AnonymousSurvey
question = "你的母语是什么？"
my_survey = AnonymousSurvey(question)  #  定义调查实例，即调查什么

while True:
      response = input("您的母语：")
      my_survey.store_response(response)  #  存储答案
my_survey.show_results()     #输出答案

'''
'''
此循环是死循环，无法结束调查，我们加一个终止调查的语句
'''
from survey import AnonymousSurvey
question = "你的母语是什么？"
my_survey = AnonymousSurvey(question)  #  定义调查实例，即调查什么

while True:
      response = input("您的母语：")
      if response == "stop":    # 注意是逻辑判断，“==”
            break
      else:
            my_survey.store_response(response)  #  存储答案
my_survey.show_results()     #输出答案

