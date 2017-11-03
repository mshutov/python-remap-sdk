import unittest
import uuid

from remap11.remap11.model.Descriptors import product
from remap11.test.BaseTest import BaseTest


class ProductTest(BaseTest):
    def test_get_list(self):
        r = self.client.list(product, limit=1, expand='')
        self.assertIn('rows', r)

    def test_create_delete_product(self):
        product_name = str(uuid.uuid4())
        p = {'name': product_name}
        r = self.create_product(p)[0]
        self.assertIn('meta', r)
        self.assertIn('href', r['meta'])
        self.assertIn('name', r)
        self.assertEqual(product_name, r['name'])
        deleted = self.client.delete_by_href(r['meta']['href'])
        self.assertTrue(deleted)

    def test_create_delete_products(self):
        number_of_products = 3
        product_sync_ids = [str(uuid.uuid4()) for _ in range(number_of_products)]
        products = [{'name': 'good {}'.format(idx), 'syncId': sync_id}
                    for (idx, sync_id) in enumerate(product_sync_ids)]
        r = self.create_product(products)
        self.assertIsInstance(r, list)
        self.assertEqual(number_of_products, len(r))
        for p in r:
            self.assertIn(p['syncId'], product_sync_ids)
            deleted = self.client.delete_by_href(p['meta']['href'])
            self.assertTrue(deleted)


if __name__ == '__main__':
    unittest.main()
