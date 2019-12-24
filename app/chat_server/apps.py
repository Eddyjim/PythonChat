"""
app.chat_server.apps
--------------------
Apps for chat_server app
"""

from django.apps import AppConfig

from chat_server.message_handlers import AMQPConsuming


class ChatServerConfig(AppConfig):
    name = 'chat_server'

    def ready(self):
        # if not settings.IS_ACCEPTANCE_TESTING and not settings.IS_UNITTESTING:
        consumer = AMQPConsuming()
        consumer.daemon = True
        consumer.start()
