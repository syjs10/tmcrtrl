#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
from pymongo import MongoClient
import json

conn = MongoClient('127.0.0.1', 27017)
db = conn.info
# mongo插入数据
def insertData(data):
    my_set = db.tmprecode
    print(data)
    data = json.loads(data)
    res = my_set.insert(data)
    print(res)
    return res
# ########################## 消费者 ##########################
credentials = pika.PlainCredentials('tmp', 'tmp')
# 连接到rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('106.12.125.225',5672,'/',credentials))
channel = connection.channel()

# 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
#channel.queue_declare(queue='wzg')


# 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
def callback(ch, method, properties, body):
    insertData(body.decode())

    # print(" [x] Received %r" % body)


# 告诉rabbitmq使用callback来接收信息
channel.basic_consume(callback,
                      queue='tmpdata',
                      no_ack=True)
 # no_ack=True表示在回调函数中不需要发送确认标识

print(' [*] Waiting for messages. To exit press CTRL+C')

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()

