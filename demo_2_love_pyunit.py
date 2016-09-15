import unittest
from demo_1_first_test import make_money

class TestMakeMoney(unittest.TestCase):
    def test_make_money(self):
        self.assertEqual(make_money(1), 101)
unittest.main()
