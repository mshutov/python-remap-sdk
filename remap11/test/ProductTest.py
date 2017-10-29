import unittest
import uuid

from remap11.remap11.model.Product import Product
from remap11.test.BaseTest import BaseTest


class ProductTest(BaseTest):
    def test_get_list(self):
        r = self.client.list(Product, limit=4, expand='')
        self.assertIn('rows', r)

    def test_create_delete_product(self):
        product_name = str(uuid.uuid4())
        p = {'name': product_name}
        r = self.client.create_or_update(Product, p)
        self.assertIn('meta', r)
        self.assertIn('href', r['meta'])
        self.assertIn('name', r)
        self.assertEqual(product_name, r['name'])
        deleted = self.client.delete_by_href(r['meta']['href'])
        self.assertTrue(deleted)

    def test_create_delete_products(self):
        number_of_products = 3
        product_names = [str(uuid.uuid4()) for _ in range(number_of_products)]
        products = [{'name': name} for name in product_names]
        r = self.client.create_or_update(Product, products)
        self.assertIsInstance(r, list)
        self.assertEqual(number_of_products, len(r))
        for p in r:
            self.assertIn(p['name'], product_names)
            deleted = self.client.delete_by_href(p['meta']['href'])
            self.assertTrue(deleted)


if __name__ == '__main__':
    unittest.main()
