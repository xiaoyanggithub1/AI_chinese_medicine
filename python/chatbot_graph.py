from question_classifier import *
from question_parser import *
from answer_search import *
import json

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        data = '我没有理解你的意思，可能是我的数据量较少，或者你可以换一种问法'
        answer = {
            'type': 0,
            'data': data,
        }
        # 模糊查询使用
        sent2 = sent.replace('可以', '').replace('疾病', '').replace('什么', '').replace('治疗', '').replace('症状', '').replace('怎么办','')\
            .replace('？', '').replace('?', '').replace('我', '').replace('得', '').replace('了', '').replace('用', '').replace('方剂', '')\
            .replace('中药', '').replace('偏方', '').replace('。', '').replace('有', '').replace('病', '')
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            res_classify2 = {'args': {sent2: ['sick_symptom']}, 'question_types': ['blur']}
            res_sql = self.parser.parser_main(res_classify2)
            # print(res_sql)
            final_answers = self.searcher.search_main(res_sql)
            print(final_answers)
            if not final_answers:
                return json.dumps(answer)
            else:
                return '\n'.join(final_answers)
        res_sql = self.parser.parser_main(res_classify)
        # print(res_sql)
        final_answers = self.searcher.search_main(res_sql)
        # print(final_answers)
        if not final_answers:
            return json.dumps(answer)
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('咨询:')
        answer = handler.chat_main(question)
