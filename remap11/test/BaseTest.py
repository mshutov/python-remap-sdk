import unittest
from os import environ

from ..remap11.Client import Client


class BaseTest(unittest.TestCase):
    def setUp(self):
        self._client = Client(**self.credentials())

    @property
    def client(self):
        return self._client

    @staticmethod
    def credentials():
        return {'login': environ.get('api_user'), 'password': environ.get('api_pass')}
