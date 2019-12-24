import csv
from http import HTTPStatus

from requests import request


class BrokerClient:

    def __init__(self, host: str):
        self.host = host

    def request_symbol(self, symbol: str) -> dict:
        """
        Request the stock values for the desired symbol
        :param symbol: symbol string
        :return: market value for the stock
        """
        payload = {
            's': symbol,
            'f': 'sd2t2ohlcv',
            'e': 'csv'
        }
        try:
            response = request('GET', self.host, params=payload)
            if response.status_code == HTTPStatus.OK:
                decoded_content = response.content.decode('utf-8')
                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                crl = list(cr)
                return dict(zip(['symbol', 'date', 'time', 'open', 'high', 'low', 'close', 'volume'], crl[0]))
            else:
                return None
        except Exception as e:
            return None
