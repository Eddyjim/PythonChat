from django.conf import settings
from requests import request


def request_stock_value(stock_symbol: str) -> None:
    """

    :param stock_symbol:
    :return:
    """
    host = settings.STOCK_BOT_HOST
    payload = {
        'symbol': stock_symbol
    }
    value = request('GET', host, params=payload)
