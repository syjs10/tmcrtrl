import pika
import time
import json

credential = pika.PlainCredentials('tmp', 'tmp')
connection = pika.BlockingConnection(pika.ConnectionParameters('106.12.125.225', 5672, '/', credential))
channel = connection.channel()
for i in range(6):
    f = open('/sys/bus/w1/drivers/w1_slave_driver/28-041780c476ff/w1_slave', 'r')
    arr=[]
    for line in f:
        arr.append(line)
    tmp  = arr[1].split("t=")[1].strip()
    tmp  = "{:.3f}".format(int(tmp) / 1000)
    data = json.dumps({'tmp': tmp, 'time': time.time()})
    f.close()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello', body=data)
    time.sleep(10)

connection.close()
