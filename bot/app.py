import falcon

from clients.broker_client import BrokerClient
from message_handlers.chat_handler import ChatMessageHandler

from middlewares import (
    ContentEncodingMiddleware,
)
from resourses import market_data


class BotAPI(falcon.API):

    def __init__(self, cfg):
        super(BotAPI, self).__init__(
            middleware=[ContentEncodingMiddleware()]
        )

        self.cfg = cfg

        # Build an object to manage our db connections.
        client = BrokerClient(self.cfg.broker.host)

        message_handler = ChatMessageHandler(self.cfg.channel['host'], self.cfg.channel['queue_name'])

        # Create our resources
        market_data_res = market_data.MarketDataResource(client, message_handler)

        # Build routes
        self.add_route('/market_data', market_data_res)

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
