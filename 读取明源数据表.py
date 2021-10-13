# -*- coding:utf-8 -*-
import json

# 导入json文件
with open("./jsonFile/销售系统数据表.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    print(type(load_dict))

# 读取过滤json文件

entitys = []

for dict in load_dict:
    entitys_dict = {}

    entity_entityId = dict['entity']['entityId']
    entity_name = dict['entity']['name']
    entity_displayName = dict['entity']['displayName']

    entity = {
        'entityId': entity_entityId,
        'name': entity_name,
        'displayName': entity_displayName,
        'attributes': []

    }

    # print(dict['entity']['entityId'])
    # print(dict['entity']['name'])
    # print(dict['entity']['displayName'])

    entity_attributes = []
    for attribute in dict['entity']['attributes']:
        attributes_name = attribute['name']
        attributes_dbType = attribute['dbType']
        attributes_displayName = attribute['displayName']

        entity_attribute = {
            'name': attributes_name,
            'dbType': attributes_dbType,
            'displayName': attributes_displayName
        }

        entity_attributes.append(entity_attribute)

        # print(attribute['name'])
        # print(attribute['dbType'])
        # print(attribute['displayName'])
    entity['attributes'] = entity_attributes

    entitys_dict['entity'] = entity
    entitys.append(entitys_dict)
    print(entitys)
    print(type(entitys))

# 导出json文件
with open("./jsonFile/销售系统数据表(简易版).json", "w") as dump_f:
    json.dump(entitys, dump_f, ensure_ascii=False)
