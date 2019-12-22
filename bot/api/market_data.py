"""
api.market_data
-------------

"""
import json

import falcon

from bot.client.StockClient import StockClient


class MarketDataAPI:
    """
    Market Data API
    """

    def on_get(self, req, resp):
        """
        Handles GET requests
        :param req: request
        :param resp: response
        :return:
        """
        values = StockClient.request_symbol(req)
        resp.body = json.dumps(values, ensure_ascii=False)
        resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route('/market_data', MarketDataAPI())
