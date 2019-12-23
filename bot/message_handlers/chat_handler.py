import json

import pika


class ChatMessageHandler:

    def __init__(self, host: str, queue_name: str):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, event: dict):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(event))

    def disconnect(self):
        self.connection.close()
