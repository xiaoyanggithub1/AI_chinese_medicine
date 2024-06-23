class QuestionPaser:
    '''构建实体节点'''

    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)
        return entity_dict

    '''解析主函数'''

    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        # print(entity_dict)
        # print(question_types)
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            # print(sql_)
            sql = []
            if question_type == 'prescription_symptom':
                sql = self.sql_transfer(question_type, entity_dict.get('prescription'))

            if question_type == 'prescription_usage':
                sql = self.sql_transfer(question_type, entity_dict.get('prescription'))

            elif question_type == 'symptom_prescription':
                sql = self.sql_transfer(question_type, entity_dict.get('symptom'))
                # print(sql)
            elif question_type == 'prescription_sick':
                sql = self.sql_transfer(question_type, entity_dict.get('prescription'))

            elif question_type == 'sick_prescription':
                sql = self.sql_transfer(question_type, entity_dict.get('sick'))

            elif question_type == 'prescription_pecipes':
                sql = self.sql_transfer(question_type, entity_dict.get('prescription'))

            elif question_type == 'pecipes_prescription':
                sql = self.sql_transfer(question_type, entity_dict.get('pecipes'))

            elif question_type == 'sick_not_food':
                sql = self.sql_transfer(question_type, entity_dict.get('sick'))

            elif question_type == 'sick_do_food':
                sql = self.sql_transfer(question_type, entity_dict.get('sick'))

            elif question_type == 'food_not_sick':
                sql = self.sql_transfer(question_type, entity_dict.get('food'))

            elif question_type == 'food_do_sick':
                sql = self.sql_transfer(question_type, entity_dict.get('food'))

            elif question_type == 'blur':
                sql = self.sql_transfer(question_type, entity_dict.get('sick_symptom'))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)
        # print(sqls)
        return sqls

    # 针对不同的问题，分开进行处理
    def sql_transfer(self, question_type, entities):
        # print(entities)
        if not entities:
            return []

        # 查询语句
        sql = []
        # 查询方剂药的用量
        if question_type == 'prescription_usage':
            sql = ["MATCH (m:Prescription) where m.name = '{0}' return m.name, m.consumption, m.usage".format(i) for i
                   in entities]

        # 查询方剂可以治疗哪些症状
        elif question_type == 'prescription_symptom':
            sql = [
                "MATCH (m:Prescription)-[r:usage]->(n:Symptoms) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 查询症状可以被哪些方剂所治疗
        elif question_type == 'symptom_prescription':
            # sql = ["MATCH (m:Prescription)-[r:usage]->(n:Symptoms) where n.name in ['{0}','疼痛'] return m.name, r.name, n.name".format(i) for i in entities]
            sql = [
                "MATCH (m:Prescription)-[r:usage]->(n:Symptoms) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 查询方剂可以治疗的疾病
        elif question_type == 'prescription_sick':
            sql = [
                "MATCH (m:Prescription)-[r:major]->(n:Sick) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 查询疾病可以被哪些方剂所治疗
        elif question_type == 'sick_prescription':
            sql = [
                "MATCH (m:Prescription)-[r:major]->(n:Sick) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 已知方剂查药品
        elif question_type == 'prescription_pecipes':
            sql = [
                "MATCH (m:Prescription)-[r:belongs_to]->(n:Pecipes) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]

        # 已知药品查方剂
        elif question_type == 'pecipes_prescription':
            sql = [
                "MATCH (m:Prescription)-[r:belongs_to]->(n:Pecipes) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            # 查询疾病的忌口

        elif question_type == 'sick_not_food':
            sql = ["MATCH (m:Sick)-[r:no_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i)
                   for i in entities]
        # 查询疾病建议吃的东西
        elif question_type == 'sick_do_food':
            sql1 = [
                "MATCH (m:Sick)-[r:do_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(i)
                for i in entities]
            sql2 = [
                "MATCH (m:Sick)-[r:recommand_eat]->(n:Food) where m.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql = sql1 + sql2

        # 已知忌口查疾病
        elif question_type == 'food_not_sick':
            sql = ["MATCH (m:Sick)-[r:no_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i)
                   for i in entities]

        # 已知推荐查疾病
        elif question_type == 'food_do_sick':
            sql1 = [
                "MATCH (m:Sick)-[r:do_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(i)
                for i in entities]
            sql2 = [
                "MATCH (m:Sick)-[r:recommand_eat]->(n:Food) where n.name = '{0}' return m.name, r.name, n.name".format(
                    i) for i in entities]
            sql = sql1 + sql2

        # 疾病和症状的模糊查询
        elif question_type == 'blur':
            sql1 = ["MATCH (m:Sick) where m.name contains '{0}' return m.name".format(i)
                    for i in entities]
            sql2 = [
                "MATCH (m:Symptoms) where m.name contains '{0}' return m.name".format(
                    i) for i in entities]
            sql = sql1 + sql2

        return sql


if __name__ == '__main__':
    handler = QuestionPaser()
    handler.parser_main()
    # a = handler.parser_main({'args': {'风湿': ['sick_symptom']}, 'question_types': ['blur']})
    # print(a)
