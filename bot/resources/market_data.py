"""
resources.market_data
"""

import falcon

from resources import BaseResource

BOT_NAME = 'stockbot'


class MarketDataResource(BaseResource):
    """
    Market Data API Resources
    """

    def on_get(self, req, resp):
        """
        Handles GET requests
        :param req: request
        :param resp: response
        :return:
        """
        values = self.broker_client.request_symbol(req.params['symbol'])
        if values:

            # resp.body = values
            resp.body = 'Ok'
            resp.status = falcon.HTTP_200
            message = f'{values["symbol"]} quote is ${values["close"]} per share'
        else:
            resp.status = falcon.HTTP_404
            message = f'No values where found for {values["symbol"]}'

        event = {
            'author': BOT_NAME,
            'room': req.params['room'],
            'message': message
        }
        self.message_handler.send_message(event)
