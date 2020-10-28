'''
单个答案的收集
'''
import unittest
from survey import AnonymousSurvey

class TestAnonmousSurvey(unittest.TestCase):   #针对Anon.类的测试
      def test_store_single_response(self):
            question = "你的母语是什么？"
            my_survey = AnonymousSurvey(question)   # 定义调查实例
            my_survey.store_response("汉语")

            self.assertIn("汉语", my_survey.responses) #核实“汉语”在my_survey.responses中

unittest.main()  # 输出OK

'''
多个答案的收集: 使用for...in...循环
'''
class TestAnonmousSurveys(unittest):
      def test_store_three_response(self):
            question = "你的母语是什么？"
            my_survey = AnonymousSurvey(question)   # 定义调查实例
            L = ["汉语", "English", "韩语"]
            for x  in L:
                  my_survey.store_response(x)
            
            for x in L:
                  self.assertIn(x, my_survey.responses)
unittest.main()   #  输出OK

###############  setUp()方法############################
