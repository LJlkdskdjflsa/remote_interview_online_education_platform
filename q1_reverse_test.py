import unittest

from q1_reverse import *
class TestReverse(unittest.TestCase):
    def test_word(self):
        self.assertAlmostEqual(reverse_word("Hi"),"iH")
        self.assertAlmostEqual(reverse_word("hello"),"olleh")

    def test_text(self):
        self.assertAlmostEqual(reverse_text("hello I am LJ"),"olleh I ma JL")
        self.assertAlmostEqual(reverse_text("I like python"),"I ekil nohtyp")

if __name__ == '__main__':
    unittest.main()