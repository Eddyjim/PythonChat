from http import HTTPStatus

from django.conf import settings
from requests import request

from chat_server.exceptions.chat_bot_exeptions import ChatBotRequestException

ENABLED_COMMANDS = {
    'stock': {
        'path': '/market_data',
        'method': 'GET',
        'params': ['symbol']
    }
}


class BotAPIClient:
    """

    """

    def __init__(self):
        self.host = settings.STOCK_BOT_HOST

    def command(self, command: str, room: str):
        """

        :param command:
        :param kwargs:
        :return:
        """
        command = command.split('=')
        values = command[1].split(',')
        if command[0] in ENABLED_COMMANDS.keys():
            payload = dict(zip(ENABLED_COMMANDS[command[0]]['params'], values))
            payload['room'] = room
            try:
                response = request(ENABLED_COMMANDS[command[0]]['method'],
                                   self.host + ENABLED_COMMANDS[command[0]]['path'],
                                   params=payload)
                if response.status_code != HTTPStatus.OK:
                    raise ChatBotRequestException
            except Exception as e:
                raise ChatBotRequestException
