__author__ = 'anthonymcclay'
__project__ = 'RabbitMQ'
__date__ = '10/15/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World! These Nutz"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()



