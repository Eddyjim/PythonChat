"""

----------------
"""
import pika

from chat_server.consumers import ChatConsumer


class SockBotQueue:

    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        queue_name = 'market_data'

        channel.queue_declare(queue=queue_name)
        # result = channel.queue_declare(queue='', exclusive=True)
        # queue_name = result.method.queue

        # channel.queue_bind(exchange='logs', queue=queue_name)

        self.consumer = ChatConsumer(scope={'url_route': {'kwargs': {'room_name'}}})
        self.consumer.connect()

        channel.basic_consume(queue=queue_name,
                              auto_ack=True,
                              on_message_callback=self.callback)

        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        event = {
            'author': 'stockbot',
            'message': body
        }
        self.consumer.chat_message(event)
