class AnonymousSurvey():   # 收集匿名问卷调查的答案

      def __init__(self, question):  
            self.question = question
            self.responses = []

      def show_question(self):
            print(self.question)

      def store_response(self, new_response):
            self.responses.append(new_response)

      def show_results(self):
            print("调查结果：")
            for x in self.responses:
                  print(x)