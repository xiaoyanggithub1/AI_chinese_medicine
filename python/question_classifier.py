import os
import ahocorasick


class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        # 　特征词路径
        self.food_path = os.path.join(cur_dir, 'dict/food.txt')
        self.sick_path = os.path.join(cur_dir, 'dict/sick.txt')
        self.prescription_path = os.path.join(cur_dir, 'dict/prescription.txt')
        self.recipes_path = os.path.join(cur_dir, 'dict/recipes.txt')
        self.symptom_path = os.path.join(cur_dir, 'dict/symptoms.txt')
        self.deny_path = os.path.join(cur_dir, 'dict/deny.txt')
        # 加载特征词
        self.food_wds = [i.strip() for i in open(self.food_path, encoding="gbk") if i.strip()]
        self.sick_wds = [i.strip() for i in open(self.sick_path, encoding="gbk") if i.strip()]  # encoding="utf-8"
        self.prescription_wds = [i.strip() for i in open(self.prescription_path, encoding="gbk") if i.strip()]
        self.recipes_wds = [i.strip() for i in open(self.recipes_path, encoding="gbk") if i.strip()]
        self.symptom_wds = [i.strip() for i in open(self.symptom_path, encoding="gbk") if i.strip()]
        self.region_words = set(self.prescription_wds + self.sick_wds + self.recipes_wds + self.symptom_wds + self.food_wds)
        self.deny_words = [i.strip() for i in open(self.deny_path, encoding="utf-8") if i.strip()]
        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()
        # 问句疑问词
        self.symptom_qwds = ['症状', '表征', '现象', '症候', '表现']
        self.fangji_qwds = ['方剂', '药方', '偏方', '中药方', '汤', '方剂方', '有什么方剂', '被什么方剂']
        self.drug_qwds = ['药', '药品', '用药', '胶囊', '口服液', '炎片']
        self.food_qwds = ['饮食', '饮用', '吃', '食', '伙食', '膳食', '喝', '菜', '忌口', '补品', '保健品', '食谱',
                          '菜谱', '食用', '食物', '补品']
        self.cureway_qwds = ['怎么治疗', '如何医治', '怎么医治', '怎么治', '怎么医', '如何治', '医治方式', '疗法',
                             '咋治', '怎么办', '咋办', '咋治']
        self.cure_qwds = ['治疗什么', '治啥', '治疗啥', '医治啥', '治愈啥', '主治啥', '主治什么', '有什么用', '有何用',
                          '用处', '用途',
                          '有什么好处', '有什么益处', '有何益处', '用来', '用来做啥', '用来作甚', '需要', '要']
        self.usage_qwds = ['用量', '用法', '怎么用', '怎么服用', '如何用', '该怎么服用', '如何服用']
        print('model init finished ......')

        return

    '''分类主函数'''

    def classify(self, question):
        data = {}
        medical_dict = self.check_medical(question)
        if not medical_dict:
            return {}
        data['args'] = medical_dict
        # 收集问句当中所涉及到的实体类型
        types = []
        for type_ in medical_dict.values():
            types += type_
        question_type = 'others'

        question_types = []

        # 症状
        if self.check_words(self.symptom_qwds, question) and ('prescription' in types):
            question_type = 'prescription_symptom'
            question_types.append(question_type)

        if self.check_words(self.fangji_qwds, question) and ('symptom' in types):
            question_type = 'symptom_prescription'
            question_types.append(question_type)
        # 方剂用法
        if self.check_words(self.usage_qwds, question) and ('prescription' in types):
            question_type = 'prescription_usage'
            question_types.append(question_type)
        # 疾病
        if self.check_words(self.cure_qwds, question) and ('prescription' in types):
            question_type = 'prescription_sick'
            question_types.append(question_type)
        if self.check_words(self.fangji_qwds, question) and ('sick' in types):
            question_type = 'sick_prescription'
            question_types.append(question_type)

        # 推荐药品
        if self.check_words(self.drug_qwds, question) and 'prescription' in types:
            question_type = 'prescription_pecipes'
            question_types.append(question_type)
        if self.check_words(self.fangji_qwds, question) and 'pecipes' in types:
            question_type = 'pecipes_prescription'
            question_types.append(question_type)

        # 推荐食品
        if self.check_words(self.food_qwds, question) and 'sick' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'sick_not_food'
            else:
                question_type = 'sick_do_food'
            question_types.append(question_type)

        # 已知食物找疾病
        if self.check_words(self.food_qwds + self.cure_qwds, question) and 'food' in types:
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'food_not_sick'
            else:
                question_type = 'food_do_sick'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'sick' in types:
            question_types = ['sick_prescription']

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'symptom' in types:
            question_types = ['symptom_prescription']

        # 将多个分类结果进行合并处理，组装成一个字典
        data['question_types'] = question_types
        return data

    '''构造词对应的类型'''

    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.food_wds:
                wd_dict[wd].append('food')
            if wd in self.sick_wds:
                wd_dict[wd].append('sick')
            if wd in self.prescription_wds:
                wd_dict[wd].append('prescription')
            if wd in self.recipes_wds:
                wd_dict[wd].append('pecipes')
            if wd in self.symptom_wds:
                wd_dict[wd].append('symptom')
        return wd_dict

    '''构造actree，加速过滤'''

    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''问句过滤'''

    def check_medical(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i: self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    '''基于特征词进行分类'''

    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('input an question:')
        data = handler.classify(question)
        # print(data)
