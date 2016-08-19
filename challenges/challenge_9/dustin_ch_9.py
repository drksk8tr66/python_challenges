import unittest
from challenges.challenge_8.dustin_ch_8 import arrange_message


class MyTestCase(unittest.TestCase):

    def test_only_numbers_ordered(self):
        x = '123'
        expected = ['1', '2', '3']
        self.assertEquals(arrange_message(1, x), expected)

    def test_only_numbers_unordered(self):
        x = '312'
        expected = ['1', '2', '3']
        self.assertEquals(arrange_message(1, x), expected)


if __name__ == '__main__':
    unittest.main()
