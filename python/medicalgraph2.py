
import os
import json
from py2neo import Graph, Node


class MedicalGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur_dir, r'data/result2.json')
        self.g = Graph("http://localhost:7474", auth=("neo4j", "159CH247"), name="neo4j")

    '''读取文件'''

    def read_nodes(self):
        # 共5类节点
        prescriptions = []  # 处方->name  drugs
        recipes = []  # 食谱->constitute  foods
        function = []  # 功能->effect   diseases
        symptoms = []  # 症状->major   symptoms
        method = []  # 用法用量->usage

        disease_infos = []  # 病症信息

        # 构建节点实体关系
        rels_doeat = []  # 症状－宜吃食谱关系
        rels_recommandeat = []  # 症状－推荐处方关系
        rels_commonddrug = []  # 处方－食谱关系
        rels_drug_method = []  # 食谱－用法用量关系  rels_drug_producer

        count = 0
        for data in open(self.data_path, encoding='utf-8'):
            prescription_dict = {}
            count += 1
            print(count)
            data_json = json.loads(data)
            prescription = data_json['name']
            prescription_dict['name'] = prescription
            prescriptions.append(prescription)
            prescription_dict['constitute'] = ''
            prescription_dict['effect'] = ''
            prescription_dict['sick'] = ''
            prescription_dict['usage'] = ''

            if 'sick' in data_json:
                prescription_dict['sick'] = data_json['sick']
                major = data_json['sick']
                symptoms += major
                for major in data_json['sick']:
                    rels_recommandeat.append([prescription, major])

            if 'constitute' in data_json:
                prescription_dict['constitute'] = data_json['constitute']
                constitute = data_json['constitute']
                recipes += constitute

            if 'effect' in data_json:
                prescription_dict['effect'] = data_json['effect']
                effect = data_json['effect']
                function += effect

            if 'usage' in data_json:
                prescription_dict['usage'] = data_json['usage']
                usage = data_json['usage']
                method += usage

            if 'consumption' in data_json:
                prescription_dict['consumption'] = data_json['consumption']
                # usage = data_json['usage']
                # method += usage

            if 'constitute' in data_json:
                do_eat = data_json['constitute']
                for _do in do_eat:
                    rels_doeat.append([prescription, _do])

            if 'effect' in data_json:
                rels_drug = data_json['effect']
                for _effect in rels_drug:
                    rels_commonddrug.append([prescription, _effect])


            if 'usage' in data_json:
                do_use = data_json['usage']
                for _use in do_use:
                    rels_drug_method.append([prescription, _use])
            disease_infos.append(prescription_dict)
            # print(rels_commonddrug)
            # print(rels_doeat)
        return set(prescriptions), set(recipes), set(function), set(symptoms), set(method), disease_infos, rels_doeat, rels_recommandeat, rels_commonddrug, rels_drug_method,\
            '''建立节点'''

    def create_node(self, label, nodes):
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.g.create(node)
            count += 1
            print(count, len(nodes))
        return

    '''创建知识图谱中心疾病的节点'''

    def create_diseases_nodes(self, disease_infos):
        count = 0
        print(disease_infos)
        for prescription_dict in disease_infos:
            node = Node("Prescription", name=prescription_dict['name'], consumption=prescription_dict['consumption'],
                        usage=prescription_dict['usage'])
            self.g.create(node)
            count += 1
            print(count)
        return

    '''创建知识图谱实体节点类型schema'''

    def create_graphnodes(self):
        Prescriptions,Recipes,Function,Symptoms,Method,disease_infos,rels_doeat,rels_recommandeat,rels_commonddrug,rels_drug_method,a= self.read_nodes()
        # print(a)
        self.create_diseases_nodes(disease_infos)
        # self.create_node('Prescription', Prescriptions)
        # print(len(Prescriptions))
        self.create_node('Symptoms', Function)
        print(len(Function))
        self.create_node('Pecipes', Recipes)
        print(len(Recipes))
        self.create_node('Sick', Symptoms)
        print(len(Symptoms))
        # self.create_node('Method', Method)
        # print(len(Method))
        return

    '''创建实体关系边'''

    def create_graphrels(self):
        Prescriptions,Recipes,Function,Symptoms,Method,disease_infos,rels_doeat,rels_recommandeat,rels_commonddrug,rels_drug_method,a= self.read_nodes()
        self.create_relationship('Prescription', 'Pecipes', rels_doeat, 'belongs_to', '组成药剂')
        self.create_relationship('Prescription', 'Symptoms', rels_commonddrug, 'usage', '方剂主治症状')
        self.create_relationship('Prescription', 'Sick', rels_recommandeat, 'major', '方剂主治疾病')

    # 创建实体关联边

    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        count = 0
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
        all = len(set(set_edges))
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.g.run(query)
                count += 1
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return

     # 导出数据

    def export_data(self):
        Prescriptions,Recipes,Function,Symptoms,Method,disease_infos,rels_doeat,rels_recommandeat,rels_commonddrug,rels_drug_method,a= self.read_nodes()
        print(Prescriptions)
        print(Recipes)
        print(Function)
        print(Symptoms)
        # print(Method)
        f_prescription = open('dict/prescription.txt', 'w+')
        f_recipes = open('dict/recipes.txt', 'w+')
        f_function = open('dict/symptoms.txt', 'w+')
        f_symptoms = open('dict/sick.txt', 'w+')
        # f_method = open('method.txt', 'w+')

        f_prescription.write('\n'.join(list(Prescriptions)))
        f_recipes.write('\n'.join(list(Recipes)))
        f_function.write('\n'.join(list(Function)))
        f_symptoms.write('\n'.join(list(Symptoms)))
        # f_method.write('\n'.join(list(Method)))

        f_prescription.close()
        f_recipes.close()
        f_function.close()
        f_symptoms.close()
        # f_method.close()

        return



if __name__ == '__main__':
    handler = MedicalGraph()
    # handler.export_data()
    handler.create_graphnodes()
    handler.create_graphrels()
    # handler.read_nodes()