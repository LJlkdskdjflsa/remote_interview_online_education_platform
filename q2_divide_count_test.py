import unittest

from q2_divide_count import *
class TestDivide(unittest.TestCase):
    def test_count(self):
        self.assertEqual(divide_count(20),11)
        self.assertEqual(divide_count(100),53)


if __name__ == '__main__':
    unittest.main()