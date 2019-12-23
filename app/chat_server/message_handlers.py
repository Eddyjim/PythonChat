"""

----------------
"""
import json
import threading

import pika
import websocket
from django.conf import settings


class AMQPConsuming(threading.Thread):
    def callback(self, ch, method, properties, body):
        event = json.loads(body)
        ws = websocket.WebSocket()
        ws.connect(f"ws://localhost:8000/ws/chat/{event['room']}/")
        ws.send(body)
        ws.close()

    @staticmethod
    def _get_connection():
        return pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST))

    def run(self):
        connection = self._get_connection()
        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)
        queue_name = settings.MARKET_DATA_QUEUE_NAME
        # channel.basic_consume(self.callback, queue=queue_name)
        channel.basic_consume(queue=queue_name,
                              auto_ack=True,
                              on_message_callback=self.callback)

        channel.start_consuming()
