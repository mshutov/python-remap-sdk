from requests import get


class Client:
    path = '/api/remap/1.1/'

    def __init__(self, login, password, host='https://online.moysklad.ru'):
        self._login = login
        self._password = password
        self._url = host + self.path

    def list(self, entity, limit=25):
        query_params = {'limit': limit}
        return get(
            self._url + 'entity/' + entity,
            auth=(self._login, self._password),
            params=query_params).json()
