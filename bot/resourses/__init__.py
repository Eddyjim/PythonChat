"""

"""
from clients.broker_client import BrokerClient
from message_handlers.chat_handler import ChatMessageHandler


class BaseResource(object):
    """

    """

    def __init__(self, broker_client: BrokerClient, message_handler: ChatMessageHandler):
        self.broker_client: BrokerClient = broker_client
        self.message_handler: ChatMessageHandler = message_handler
