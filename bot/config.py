from aumbry import Attr, YamlConfig


class BrokerConfig(YamlConfig):
    __mapping__ = {
        'host': Attr('host', str),
    }

    connection = ''


class AppConfig(YamlConfig):
    __mapping__ = {
        'broker': Attr('broker', BrokerConfig),
        'gunicorn': Attr('gunicorn', dict),
        'channel': Attr('channel', dict),
    }

    def __init__(self):
        self.broker = BrokerConfig()
        self.gunicorn = {}