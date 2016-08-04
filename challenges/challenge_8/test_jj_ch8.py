import unittest
from challenges.challenge_8.jj_ch_8 import order_list


class MyTestCase(unittest.TestCase):

    def test_only_numbers_ordered(self):
        x = ['1', '2', '3']
        expected = ['1', '2', '3']
        self.assertEquals(order_list(x),expected)

    def test_only_numbers_unordered(self):
        x = ['2', '3', '1']
        expected = ['1', '2', '3']
        self.assertEquals(order_list(x),expected)

    def test_only_letters_ordered(self):
        x = ['a', 'b', 'z']
        expected = ['a', 'b', 'z']
        self.assertEquals(order_list(x), expected)

    def test_only_letters_unordered(self):
        x = ['z', 'x', 'y']
        expected = ['x', 'y', 'z']
        self.assertEquals(order_list(x), expected)

    def test_letters_floats_ints_ordred(self):
        x = ['0.1', '1', 'a', 'b']
        expected = ['0.1', '1', 'a', 'b']
        self.assertEquals(order_list(x), expected)

    def test_letters_floats_ints_unordered(self):
        x = ['1', '0.1', 'b', 'a']
        expected =  ['0.1', '1', 'a', 'b']
        self.assertEquals(order_list(x), expected)

if __name__ == '__main__':
    unittest.main()
