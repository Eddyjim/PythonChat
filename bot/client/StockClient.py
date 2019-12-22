from requests import request


class StockClient:
    host = 'https://stooq.com/q/l/'

    @classmethod
    def request_symbol(cls, symbol: str) -> dict:
        """
        Request the stock values for the desired symbol
        :param symbol: symbol string
        :return: market value for the stock
        """
        payload = {
            's': symbol,
            'f': 'sd2t2ohlcv',
            'e': 'json'
        }
        response = request('GET', cls.host, params=payload)

        return response.json()['symbols'][0]
