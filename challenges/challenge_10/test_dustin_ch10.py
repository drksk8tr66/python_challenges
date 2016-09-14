import unittest
from challenges.challenge_10.dustin_ch_10 import validate
from challenges.challenge_10.nicole_ch_10 import validate_phone_number
from challenges.challenge_10.jj_ch_10 import PhoneCheck


class MyTestCase(unittest.TestCase):

    def test_only_7_digits(self):
        x = '1234567'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_only_10_digits(self):
        x = '1234567890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_7_digits_hyphen(self):
        x = '123-4567'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_1_hyphen(self):
        x = '123456-7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_2_hyphen(self):
        x = '123-456-7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_parens(self):
        x = '(123)4567890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_parens_1_hyphen(self):
        x = '(123)456-7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_parens_space_hyphen(self):
        x = '(123) 456-7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_spaces(self):
        x = '123 456 7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_7_digits_dots(self):
        x = '123.4567'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_10_digits_dots(self):
        x = '123.456.7890'
        expected = True
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_6_digits(self):
        x = '123456'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_8_digits(self):
        x = '12345678'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_7_characters(self):
        x = 'abcdefg'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_11_digits(self):
        x = '12345678901'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_9_digits(self):
        x = '123-45-6789'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_7_digits_colon(self):
        x = '123:4567'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_7_digits_slash(self):
        x = '123/4567'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_10_digits_mixed(self):
        x = '123-456.7890'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)

    def test_invalid_10_digits_mixed_reversed(self):
        x = '123.456-7890'
        expected = False
        self.assertEquals(validate(x), expected)
        self.assertEquals(validate_phone_number(x), expected)
        self.assertEquals(PhoneCheck().validate(x), expected)


if __name__ == '__main__':
    unittest.main()
