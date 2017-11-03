import unittest

from remap11.remap11.RemapQL import Query, New, QueryFactory
from remap11.remap11.model.Descriptors import product
from remap11.test.BaseTest import BaseTest


class ProductRemapQLTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.qf = QueryFactory(self.client)

    def test_select_name(self):
        q = Query(product, self.client).select(product.name)
        self.assertEqual(1, len(q._fields))

    def test_query_return_list(self):
        q = self.qf.query(product).select(product.name).list()
        self.assertIsInstance(q, list)

    def test_query_return_non_empty_list(self):
        product_href = self.qf.new(product).set((product.name, 'test good')).execute()['meta']['href']
        q = self.qf.query(product).select(product.name).list()
        self.assertIsInstance(q, list)
        self.assertTrue(len(q) > 0)
        self.delete(product_href)


if __name__ == '__main__':
    unittest.main()
