from py2neo import Graph
import json


class AnswerSearcher:
    def __init__(self):
        self.g = Graph('http://localhost:7474/', auth=("neo4j", "159CH247"), name='neo4j')
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
                return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):

        final_answer = {}
        if not answers:
            return ''
        if question_type == 'prescription_symptom':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            # final_answer = '{0}可以治疗的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety':1,
                'orig': subject,
                'data': '{0}可以治疗的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            }

        elif question_type == 'symptom_prescription':
            data = {}
            orig = ''
            for answer in answers:
                # print(answer['m.name'])
                symptom_prescription = "MATCH (m:Prescription)-[r:usage]->(n:Symptoms) where m.name = '{0}' return m.name, r.name, n.name".format(
                    answer['m.name'])
                result = self.g.run(symptom_prescription).data()
                # print(result)
                desc = [i['m.name'] for i in answers]
                subject1 = answers[0]['n.name']
                final_answer = '症状{0}可以使用的方剂有：{1}'.format(subject1,
                                                                    '；'.join(list(set(desc))[:self.num_limit]))
                # print(final_answer)
                desc = [i['n.name'] for i in result]
                subject2 = result[0]['m.name']
                final_answer2 = '{0}推荐的方剂有{1}可以治疗的症状包括：{2}'.format(subject1, subject2,
                                                                                  '；'.join(
                                                                                      list(set(desc))[:self.num_limit]))
                data1 = {
                    subject2: ','.join(list(set(desc))[:self.num_limit]),
                }
                data.update(data1)
                orig = subject1
            final_answer = {
                'type': 2,
                'variety': 2,
                'orig': orig,
                'data': data,
            }
            # print(data)
                # print(final_answer2)

        elif question_type == 'prescription_usage':
            consumption = [i['m.consumption'] for i in answers]
            usage = [i['m.usage'] for i in answers]
            subject = answers[0]['m.name']
            # final_answer = '{0}药品及用量分别为：{1}\n用法用量为：{2}'.format(subject, ';'.join(
            #     list(set(consumption))[:self.num_limit]), ';'.join(list(set(usage))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 3,
                'orig': subject,
                'data': '{0}药品及用量分别为：{1}\n用法用量为：{2}'.format(subject, ';'.join(
                    list(set(consumption))[:self.num_limit]), ';'.join(list(set(usage))[:self.num_limit]))
            }

        elif question_type == 'prescription_sick':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}可以治疗的疾病为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 4,
                'orig': subject,
                'data': '{0}可以治疗的疾病为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            }

        elif question_type == 'sick_prescription':
            data = {}
            orig = ''
            for answer in answers:
                # print(answer['m.name'])
                symptom_prescription = "MATCH (m:Prescription)-[r:usage]->(n:Symptoms) where m.name = '{0}' return m.name, r.name, n.name".format(
                    answer['m.name'])
                result = self.g.run(symptom_prescription).data()
                # print(result)
                desc = [i['m.name'] for i in answers]
                subject1 = answers[0]['n.name']
                final_answer = '症状{0}可以使用的方剂有：{1}'.format(subject1,
                                                                    '；'.join(list(set(desc))[:self.num_limit]))
                # print(final_answer)
                desc = [i['n.name'] for i in result]
                subject2 = result[0]['m.name']
                final_answer2 = '{0}推荐的方剂有{1}可以治疗的症状包括：{2}'.format(subject1, subject2,
                                                                                  '；'.join(
                                                                                      list(set(desc))[:self.num_limit]))
                data1 = {
                    subject2: ','.join(list(set(desc))[:self.num_limit]),
                }
                data.update(data1)
                orig = subject1
            final_answer = {
                'type': 2,
                'variety': 5,
                'orig': orig,
                'data': data,
            }


        elif question_type == 'prescription_pecipes':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            # final_answer = '{0}的药品有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 6,
                'orig': subject,
                'data': '{0}的药品有:{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            }

        elif question_type == 'pecipes_prescription':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            # final_answer = '{0}药品被：{1}所用'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 7,
                'orig': subject,
                'data': '{0}药品被：{1}所用'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            }


        elif question_type == 'sick_not_food':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            # final_answer = '{0}忌食的食物包括有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 8,
                'orig': subject,
                'data': '{0}忌食的食物包括有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            }

        elif question_type == 'sick_do_food':
            do_desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃']
            recommand_desc = [i['n.name'] for i in answers if i['r.name'] == '推荐食谱']
            subject = answers[0]['m.name']
            # final_answer = '{0}宜食的食物包括有：{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(
            #     list(set(do_desc))[:self.num_limit]), ';'.join(list(set(recommand_desc))[:self.num_limit]))
            final_answer = {
                'type': 1,
                'variety': 9,
                'orig': subject,
                'data': '{0}宜食的食物包括有：{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(
                    list(set(do_desc))[:self.num_limit]), ';'.join(list(set(recommand_desc))[:self.num_limit]))
            }

        elif question_type == 'food_not_sick':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = {
                'type': 1,
                'variety': 10,
                'orig': subject,
                'data': '患有{0}的人最好不要吃{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)
            }

        elif question_type == 'food_do_sick':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = {
                'type': 1,
                'variety': 11,
                'orig': subject,
                'data': '患有{0}的人建议多试试{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)
            }
        # 疾病和症状的模糊查询

        elif question_type == 'blur':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = {
                'type': 1,
                'variety': 12,
                'orig': subject,
                'data': '{0}'.format('；'.join(list(set(desc))[:self.num_limit]))
            }
        return json.dumps(final_answer)

if __name__ == '__main__':
    searcher = AnswerSearcher()
