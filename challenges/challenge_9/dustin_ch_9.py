import unittest
from challenges.challenge_8.dustin_ch_8 import arrange_msg
from challenges.challenge_8.nicole_ch_8 import sort_list
from challenges.challenge_8.jj_ch_8 import order_list

class MyTestCase(unittest.TestCase):

    def test_only_numbers_ordered(self):
        x = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_numbers_unordered(self):
        x = [2, 1, 3]
        expected = [1, 2, 3]
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_string_ordered(self):
        x = '123abc'
        expected = ['1', '2', '3', 'a', 'b', 'c']
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_string_unordered(self):
        x = 'acb132'
        expected = ['1', '2', '3', 'a', 'b', 'c']
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_int_string_ordered(self):
        x = [1, 2, 3, 'a', 'b', 'c']
        expected = [1, 2, 3, 'a', 'b', 'c']
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_int_string_unordered(self):
        x = [3, 'a', 2, 'c', 'b', 1]
        expected = [1, 2, 3, 'a', 'b', 'c']
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_complex_ordered(self):
        x = [(1.0+1.0j), (-2.0+1.0j), (-1.0+0.0j)]
        expected = [0.7853981633974483, 2.677945044588987, 3.141592653589793]
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_complex_unordered(self):
        x = [(-1.0 + 0.0j), (1.0 + 1.0j), (-2.0 + 1.0j)]
        expected = [0.7853981633974483, 2.677945044588987, 3.141592653589793]
        self.assertEquals(arrange_msg(x), expected)
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(order_list(x), expected)


if __name__ == '__main__':
    unittest.main()
