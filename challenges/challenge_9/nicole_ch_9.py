'''
Unit Testing for Sorting
https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
'''

import unittest
from challenges.challenge_8.nicole_ch_8 import sort_list
from challenges.challenge_8.dustin_ch_8 import arrange_message
from challenges.challenge_8.jj_ch_8 import order_list


class test_sort(unittest.TestCase):

    def test_only_integers_ordered(self):
        x = ['1', '2', '10']
        expected = ['1', '2', '10']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_integers_unordered(self):
        x = ['10', '1', '2']
        expected = ['1', '2', '10']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_integers_mixed_negatives_ordered(self):
        x = ['-10', '-2', '-1', '0', '1', '2', '10']
        expected = ['-10', '-2', '-1', '0', '1', '2', '10']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_integers_mixed_negatives_unordered(self):
        x = ['10', '-2', '0', '-1', '2', '-10', '1']
        expected = ['-10', '-2', '-1', '0', '1', '2', '10']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_floats_ordered(self):
        x = ['1.1', '1.2', '2.1', '2.2', '10.1', '10.2']
        expected = ['1.1', '1.2', '2.1', '2.2', '10.1', '10.2']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_floats_unordered(self):
        x = ['2.2', '10.1', '1.2', '2.1', '10.2', '1.1']
        expected = ['1.1', '1.2', '2.1', '2.2', '10.1', '10.2']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_floats_mixed_negatives_ordered(self):
        x = ['-10.2', '-10.1', '-2.2', '-1.1', '0', '1.1', '2.2', '10.1', '10.2']
        expected = ['-10.2', '-10.1', '-2.2', '-1.1', '0', '1.1', '2.2', '10.1', '10.2']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_floats_mixed_negatives_unordered(self):
        x = ['10.2', '-10.1', '2.2', '-1.1', '0', '1.1', '-2.2', '10.1', '-10.2']
        expected = ['-10.2', '-10.1', '-2.2', '-1.1', '0', '1.1', '2.2', '10.1', '10.2']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_numbers_mixed_ordered(self):
        x = ['-10.1', '-10', '-2.1', '-2', '-1.1', '0', '1.1', '2', '2.1', '10', '10.1']
        expected = ['-10.1', '-10', '-2.1', '-2', '-1.1', '0', '1.1', '2', '2.1', '10', '10.1']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_numbers_mixed_unordered(self):
        x = ['10.1', '-10', '2.1', '-2', '1.1', '0', '-1.1', '2', '-2.1', '10', '-10.1']
        expected = ['-10.1', '-10', '-2.1', '-2', '-1.1', '0', '1.1', '2', '2.1', '10', '10.1']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_letters_ordered(self):
        x = ['a', 'b', 'c']
        expected = ['a', 'b', 'c']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_letters_unordered(self):
        x = ['c', 'a', 'b']
        expected = ['a', 'b', 'c']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_words_ordered(self):
        x = ['apple', 'banana', 'carrot']
        expected = ['apple', 'banana', 'carrot']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_only_words_unordered(self):
        x = ['carrot', 'apple', 'banana']
        expected = ['apple', 'banana', 'carrot']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_numbers_letters_words_ordered(self):
        x = ['-10', '-2', '-1', '1', '2', '10', 'a1', 'apple', 'b1', 'b2', 'banana']
        expected = ['-10', '-2', '-1', '1', '2', '10', 'a1', 'apple', 'b1', 'b2', 'banana']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)

    def test_numbers_letters_words_unordered(self):
        x = ['apple', 'banana', 'a1', '10', '-2', 'b2', '1', '-1', 'b1', '2', '-10']
        expected = ['-10', '-2', '-1', '1', '2', '10', 'a1', 'apple', 'b1', 'b2', 'banana']
        self.assertEquals(sort_list(x), expected)
        self.assertEquals(arrange_message(x), expected)
        self.assertEquals(order_list(x), expected)


if __name__ == '__main__':
    unittest.main()
