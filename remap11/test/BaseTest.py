import unittest
from os import environ

from remap11.remap11.model.Descriptors import product
from ..remap11.Client import Client


class BaseTest(unittest.TestCase):
    def setUp(self):
        self._client = Client(**self.credentials())

    @property
    def client(self):
        return self._client

    def create_product(self, *products):
        response = self.client.create_or_update(product, products)
        self.assertNotIn('errors', response)
        return response

    def delete(self, *href_list):
        for href in href_list:
            self.client.delete_by_href(href)

    @staticmethod
    def credentials():
        return {'login': environ.get('api_user'), 'password': environ.get('api_pass')}
