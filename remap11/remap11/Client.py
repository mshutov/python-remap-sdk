from requests import get, post, delete

from remap11.remap11.model.Descriptors import Desc


class Client:
    def __init__(self, login, password, host='https://online.moysklad.ru', path='/api/remap/1.1/'):
        self._login = login
        self._password = password
        self._url = host + path

    def list(self, entity: Desc, limit=25, expand=''):
        query_params = {'limit': limit, 'expand': expand}
        return get(
            self._url + entity.path,
            auth=(self._login, self._password),
            params=query_params).json()

    def href(self, href: str):
        return get(href, auth=(self._login, self._password)).json()

    def create_or_update(self, entity_type: Desc, entity):
        return post(self._url + entity_type.path, auth=(self._login, self._password), json=entity).json()

    def delete_by_href(self, href):
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        return delete(href, auth=(self._login, self._password), headers=headers).status_code == 200
