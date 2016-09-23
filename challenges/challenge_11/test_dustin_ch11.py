import unittest
from challenges.challenge_11.dustin_ch_11 import convert


class MyTestCase(unittest.TestCase):

    def test_only_7_digits(self):
        d = 23
        m = 9
        y = 2016
        expected = 'Friday'
        self.assertEquals(convert(d, m, y), expected)

    def test_only_10_digits(self):
        d = 'Jan'
        m = 9
        y = 2016
        expected = 'Invalid Date'
        self.assertEquals(convert(d, m, y), expected)


if __name__ == '__main__':
    unittest.main()
