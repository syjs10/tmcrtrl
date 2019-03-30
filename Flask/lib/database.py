from pymongo import MongoClient
import datetime
import time
import dateutil.parser
import json
import re
conn = MongoClient('127.0.0.1', 27017)
db = conn.info


# 插入数据
def insertData(data):
    my_set = db.tmprecode
    print(data)
    data = json.loads(data)
    res = my_set.insert(data)

    return "123"

def getData():
    dataList = []
    my_set = db.tmprecode
    for data in my_set.find({},{'_id': 0}).sort('time', -1).limit(10):
        data['tmp'] =float(data['tmp'])
        dataList.append(data)
    return json.dumps(dataList)
# def insertData(school, dataList):
#     my_set = db.school
#     for one in dataList:
#         one['school']=school
#         one['date'] = dateutil.parser.parse(one['date']).strftime("%Y-%m-%d")
#         my_set.update(one, {'$set':one}, True)
# # 按学校获取数据
# def getData(school):
#     dataList = []
#     my_set = db.school
#     for data in my_set.find({'school':school}):
#         dataList.append(data)
#     return dataList
# def getNewData():
#     dataList = []
#     my_set = db.school
#     for data in my_set.find():
#         dataList.append(data)
#     dataList.sort(key=lambda data:data['date'], reverse=True)
#     return dataList
# def searchData(keyword):
#     dataList = []
#     my_set = db.school
#     for data in my_set.find({'title':{'$regex':keyword}}):
#         dataList.append(data)
#     return dataList
