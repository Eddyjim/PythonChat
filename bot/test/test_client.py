import mock

from clients.broker_client import BrokerClient


class ContentStub:
    def decode(self, _):
        return self

    def splitlines(self):
        return None


class ResponseStub:
    status_code = 200
    content = ContentStub()


class BadResponseStub:
    status_code = 404


@mock.patch('clients.broker_client.request')
@mock.patch('clients.broker_client.csv')
def test_request_symbol(mock_reader, mock_response):
    fake_values = ['AAPL.US', '2019-12-23', '22:00', 10, 280.53, 284.25, 280.3735, 284, 24561175]
    mock_response.return_value = ResponseStub()
    client = BrokerClient('')
    response = client.request_symbol('aapl.us')
    mock_reader.reader.return_value = fake_values
    expected_response = dict(zip(['symbol', 'date', 'time', 'open', 'high', 'low', 'close', 'volume'], fake_values))
    assert response == expected_response


@mock.patch('clients.broker_client.request')
def test_request_symbol_bad_response(mock_response):
    mock_response.return_value = BadResponseStub()
    client = BrokerClient('')
    response = client.request_symbol('aapl.us')
    assert response == None
