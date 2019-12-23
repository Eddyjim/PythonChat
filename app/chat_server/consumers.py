"""
app.chat_server.consumers
-------------------------
Consumers for chat_server application
"""
from datetime import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
import json

from chat_server.exceptions.chat_bot_exeptions import ChatBotRequestException
from chat_server.helpers.bot_client import BotAPIClient
from chat_server.utils.stockbot_client import request_stock_value


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bot_client = BotAPIClient()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        author = text_data_json['author']
        message = text_data_json['message']
        type = 'command' if message.startswith('/') else 'chat_message'

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': type,
                'author': author,
                'message': message if type == 'chat_message' else message[1:len(message)]
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        author = event['author']
        # Send message to WebSocket

        await self.send(text_data=json.dumps({
            'author': author,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'message': message
        }))

    async def command(self, event):
        try:
            self.bot_client.command(event['message'], self.room_name)
        except ChatBotRequestException as e:
            message = 'Bad command'
