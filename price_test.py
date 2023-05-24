import unittest
from price import calculate

class TestPricing(unittest.TestCase):
    def test_calculate(self):
        items = (
            {'case': 'No tax, no discount', 'price': 10, 'tax': 0, 'discount': 0, 'net_price': 10},
            {'case': 'Has tax, no discount', 'price': 10, 'tax': 0.1, 'discount': 0, 'net_price': 11},
            {'case': 'No tax, has discount', 'price': 10, 'tax': 0, 'discount': 1, 'net_price': 9},
            {'case': 'Has tax, has discount', 'price': 10, 'tax': 0.1, 'discount': 1, 'net_price': 9.9},
        )

        for idx in range(len(items)):
            with self.subTest(items[idx]['case']):
                self.assertEqual(calculate(items[idx]['price'], items[idx]['tax'], items[idx]['discount']), items[idx]['net_price'])