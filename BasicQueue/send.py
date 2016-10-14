__author__ = 'anthonymcclay'
__project__ = 'RabbitMQ'
__date__ = '10/12/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")


connection.close()

