# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from pprint import pprint


class InstaparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.instagram

    def process_item(self, item, spider):

        collection = self.mongo_base[spider.name]
        # pass
        collection.insert_one(item)
        # print()
        return item


# -----��������� ������ pipelines -----------

# ������������� ����� ������ ������ �� ������������ ���� ���� �������� / ����������� (����� ���� ������� � ���� ���� ���� �������)

def query(query_user, query_type):
    # ������� ������ ���������� � ������ pprint
    if query_type == 'podpiska':
        variant = 'podpiska_name'
    else:
        variant = 'podpischik_name'

    client = MongoClient('localhost', 27017)
    db = client.instagram
    collection = db.instagram

    for el in collection.find({'type_data': query_type, 'username': query_user}):
        pprint('������������: '+ ' ' + el['username'] + ' / ' + query_type + ' / ' + el[variant])

# ������� �������� ���������� ������������
query('kolia.baran','podpiska')

# ������� ����������� ������� ���������� ������������

query('babai.vasia','podpischik')