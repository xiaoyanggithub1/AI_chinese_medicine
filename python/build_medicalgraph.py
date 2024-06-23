#选材自开源项目(刘焕勇，中国科学院软件研究所)，数据集来自互联网爬虫数据
import os
import json
from py2neo import Graph,Node

class MedicalGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur_dir, r'data/result.json')
        self.g = Graph('http://localhost:7474/', auth=("neo4j", "159CH247"), name='neo4j')

    '''读取文件'''
    def read_nodes(self):
        # 共７类节点
        drugs = [] # 药品
        foods = [] #　食物
        diseases = [] #疾病
        effect = []#症状
        constitute = []  # 症状
        disease_infos = []#疾病信息

        # 构建节点实体关系

        rels_doeat = [] # 疾病－宜吃食物关系
        rels_commonddrug = [] # 疾病－通用药品关系
        rels_check = [] # 疾病－检查关系
        rels_effect = [] #疾病症状关系
        rels_constitute = []  # 疾病症状关系

        count = 0
        for data in open(self.data_path):
            disease_dict = {}
            count += 1
            print(count)
            data_json = json.loads(data)
            disease = data_json['name']
            disease_dict['name'] = disease
            diseases.append(disease)
            disease_dict['usage'] = ''
            disease_dict['major'] = ''
            disease_dict['easy_get'] = ''
            disease_dict['cure_way'] = ''
            disease_dict['effect'] = ''
            disease_dict['constitute'] = ''


            if 'effect' in data_json:
                effect += data_json['effect']
                for effect in data_json['effect']:
                    rels_effect.append([disease, effect])

            if 'constitute' in data_json:
                constitute += data_json['constitute']
                for constitute in data_json['constitute']:
                    rels_constitute.append([disease, constitute])

            if 'usage' in data_json:
                disease_dict['usage'] = data_json['usage']

            if 'major' in data_json:
                disease_dict['major'] = data_json['major']

            if 'easy_get' in data_json:
                disease_dict['easy_get'] = data_json['easy_get']

            if 'common_drug' in data_json:
                common_drug = data_json['common_drug']
                for drug in common_drug:
                    rels_commonddrug.append([disease, drug])
                drugs += common_drug
            disease_infos.append(disease_dict)
            print(disease_infos)
        return set(drugs), set(foods),  set(effect),  set(constitute),set(diseases), disease_infos,\
               rels_check, rels_doeat, rels_commonddrug,\
               rels_effect, rels_constitute,

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
        for disease_dict in disease_infos:
            print(disease_infos)
            node = Node("Disease", name=disease_dict['name'], usage=disease_dict['usage'],
                        major=disease_dict['major'] ,cause=disease_dict['cause'],
                        easy_get=disease_dict['easy_get'],
                        cure_department=disease_dict['cure_department']
                        ,cure_way=disease_dict['cure_way'] , cured_prob=disease_dict['cured_prob'])
            self.g.create(node)
            count += 1
            print(count)
        return

    '''创建知识图谱实体节点类型schema'''
    def create_graphnodes(self):
        Drugs, Foods, Checks, Departments, Producers, effect,constitute, Diseases, disease_infos,rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug,rels_effect, rels_constitute, rels_acompany, rels_category = self.read_nodes()
        self.create_diseases_nodes(disease_infos)
        self.create_node('Drug', Drugs)
        print(len(Drugs))
        self.create_node('Food', Foods)
        print(len(Foods))
        self.create_node('Check', Checks)
        print(len(Checks))
        self.create_node('Department', Departments)
        print(len(Departments))
        self.create_node('Producer', Producers)
        print(len(Producers))
        self.create_node('effect', effect)
        self.create_node('constitute', constitute)
        return


    '''创建实体关系边'''
    def create_graphrels(self):
        Drugs, Foods, Checks, Departments, Producers, effect, constitute, Diseases, disease_infos, rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug, rels_effect, rels_constitute, rels_acompany, rels_category = self.read_nodes()
        self.create_relationship('Disease', 'Food', rels_doeat, 'do_eat', '宜吃')
        self.create_relationship('Disease', 'Drug', rels_commonddrug, 'common_drug', '常用药品')
        self.create_relationship('Disease', 'Check', rels_check, 'need_check', '诊断检查')
        self.create_relationship('Disease', 'effect', rels_effect, 'has_effect', '症状')
        self.create_relationship('Disease', 'constitute', rels_constitute, 'has_constitute', '症状')




    '''创建实体关联边'''
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

    '''导出数据'''
    def export_data(self):
        Drugs, Foods, Checks, Departments, Producers, effect, Diseases, disease_infos, rels_check, rels_recommandeat, rels_noteat, rels_doeat, rels_department, rels_commonddrug, rels_drug_producer, rels_recommanddrug, rels_symptom, rels_acompany, rels_category = self.read_nodes()
        f_drug = open('drug.txt', 'w+')
        f_food = open('food.txt', 'w+')
        f_check = open('check.txt', 'w+')
        f_department = open('department.txt', 'w+')
        f_producer = open('producer.txt', 'w+')
        f_effect = open('effect.txt', 'w+')
        f_disease = open('disease.txt', 'w+')

        f_drug.write('\n'.join(list(Drugs)))
        f_food.write('\n'.join(list(Foods)))
        f_check.write('\n'.join(list(Checks)))
        f_department.write('\n'.join(list(Departments)))
        f_producer.write('\n'.join(list(Producers)))
        f_effect.write('\n'.join(list(effect)))
        f_disease.write('\n'.join(list(Diseases)))

        f_drug.close()
        f_food.close()
        f_check.close()
        f_department.close()
        f_producer.close()
        f_effect.close()
        f_disease.close()

        return



if __name__ == '__main__':
    handler = MedicalGraph()
    #handler.export_data()
    handler.create_graphnodes()
    handler.create_graphrels()
