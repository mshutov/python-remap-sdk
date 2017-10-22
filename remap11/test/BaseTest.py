import unittest
from os import environ
from ..remap11.client import Client


class TestBaseMethods(unittest.TestCase):
    def test_get_list(self):
        c = Client(**self.credentials())
        r = c.list('product', limit=1)
        assert 'rows' in r

    @staticmethod
    def credentials():
        return {'login': environ.get('api_user'), 'password': environ.get('api_pass')}


if __name__ == '__main__':
    unittest.main()
