import unittest
from challenges.challenge_11.dustin_ch_11 import convert
from challenges.challenge_11.nicole_ch_11 import get_day_of_week


class MyTestCase(unittest.TestCase):

    def test_friday_current(self):
        d = 23
        m = 9
        y = 2016
        expected = 'Friday'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)

    def test_invalid_month(self):
        d = 23
        m = 'September'
        y = 2016
        expected = 'Invalid Date'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)

    def test_day_1(self):
        d = 1
        m = 1
        y = 1
        expected = 'Monday'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)

    def test_day_leap(self):
        d = 29
        m = 2
        y = 2016
        expected = 'Monday'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)

    def test_day_not_leap(self):
        d = 29
        m = 2
        y = 2015
        expected = 'Invalid Date'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)

    def test_day_last(self):
        d = 31
        m = 12
        y = 9999
        expected = 'Friday'
        self.assertEquals(convert(d, m, y), expected)
        self.assertEquals(get_day_of_week(d, m, y), expected)


if __name__ == '__main__':
    unittest.main()
