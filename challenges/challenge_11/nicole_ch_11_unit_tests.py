'''
Unit Testing for Given Date, Get Day of Week
https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
'''

import unittest
from challenges.challenge_11.nicole_ch_11 import get_day_of_week
from challenges.challenge_11.dustin_ch_11 import convert


class test_day_of_week(unittest.TestCase):
    def test_valid_date(self):
        d = 5
        m = 9
        y = 2016
        expected = 'Monday'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_day(self):
        d = 31
        m = 9
        y = 2016
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_month(self):
        d = 5
        m = 13
        y = 2016
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_year(self):
        d = 5
        m = 9
        y = -1
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_float(self):
        d = 5
        m = 9
        y = 2016.5
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_string(self):
        d = 5
        m = 'September'
        y = 2016
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_valid_leap_year(self):
        d = 29
        m = 2
        y = 2000
        expected = 'Tuesday'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)

    def test_invalid_leap_year(self):
        d = 29
        m = 2
        y = 1999
        expected = 'Invalid Date'
        self.assertEquals(get_day_of_week(d, m, y), expected)
        self.assertEquals(convert(d, m, y), expected)


if __name__ == '__main__':
    unittest.main()
