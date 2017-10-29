from requests import get, post, delete

from typing import Type

from remap11.remap11.model.Resource import Resource


class Client:
    path = '/api/remap/1.1/'

    def __init__(self, login, password, host='https://online.moysklad.ru'):
        self._login = login
        self._password = password
        self._url = host + self.path

    def list(self, entity: Type[Resource], limit=25, expand=''):
        query_params = {'limit': limit, 'expand': expand}
        return get(
            self._url + 'entity/' + entity.path(),
            auth=(self._login, self._password),
            params=query_params).json()

    def href(self, href: str):
        return get(href, auth=(self._login, self._password)).json()

    def create_or_update(self, entity_type: Type[Resource], entity):
        return post(self._url + 'entity/' + entity_type.path(), auth=(self._login, self._password), json=entity).json()

    def delete_by_href(self, href):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        return delete(href, auth=(self._login, self._password), headers=headers).status_code == 200
